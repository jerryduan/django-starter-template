from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import AnonRateThrottle
import logging
from django.db import connection
from django.core.cache import cache
from redis import Redis
from django.conf import settings
from .decorators import monitor_performance

logger = logging.getLogger(__name__)


class PingRateThrottle(AnonRateThrottle):
    rate = "10/minute"


from .tasks import test_task


@extend_schema(
    description="Handles a ping request to check if the server is responsive.",
    responses={
        200: {
            "type": "object",
            "properties": {"ping": {"type": "string"}},
            "example": {"ping": "pong"},
        },
        405: {
            "type": "object",
            "properties": {"detail": {"type": "string"}},
            "example": {"detail": 'Method "POST" not allowed.'},
        },
    },
)
@api_view(["GET"])
@throttle_classes([PingRateThrottle])
def ping(request):
    logger.info("Ping request received from %s", request.META.get("REMOTE_ADDR"))
    return JsonResponse({"ping": "pong"})


def fire_task(request):
    """
    TODO 🚫 After testing the view, remove it with the task and the route.

    Handles a request to fire a test Celery task. The task will be retried
    up to 3 times and after 5 seconds if it fails (by default). The retry
    time will be increased exponentially.
    """
    if request.method == "GET":
        test_task.delay()
        return JsonResponse({"task": "Task fired"})

    return JsonResponse({"error": "Method Not Allowed"}, status=405)


@extend_schema(
    description=(
        "Health check endpoint that verifies the status of all system components."
    ),
    responses={
        200: {
            "type": "object",
            "properties": {
                "status": {"type": "string"},
                "database": {"type": "object"},
                "cache": {"type": "object"},
                "redis": {"type": "object"},
            },
        },
        503: {
            "type": "object",
            "properties": {
                "status": {"type": "string"},
                "error": {"type": "string"},
            },
        },
    },
)
@api_view(["GET"])
@monitor_performance
def health_check(request):
    health_status = {
        "status": "healthy",
        "database": {"status": "healthy"},
        "cache": {"status": "healthy"},
        "redis": {"status": "healthy"},
    }

    # Check database
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        health_status["database"]["status"] = "healthy"
    except Exception as e:
        health_status["database"]["status"] = "unhealthy"
        health_status["database"]["error"] = str(e)
        health_status["status"] = "unhealthy"

    # Check cache
    try:
        cache.set("health_check", "ok", 1)
        if cache.get("health_check") == "ok":
            health_status["cache"]["status"] = "healthy"
        else:
            health_status["cache"]["status"] = "unhealthy"
            health_status["cache"]["error"] = "Cache get/set failed"
            health_status["status"] = "unhealthy"
    except Exception as e:
        health_status["cache"]["status"] = "unhealthy"
        health_status["cache"]["error"] = str(e)
        health_status["status"] = "unhealthy"

    # Check Redis if configured
    if hasattr(settings, "REDIS_URL"):
        try:
            redis_client = Redis.from_url(settings.REDIS_URL)
            redis_client.ping()
            health_status["redis"]["status"] = "healthy"
        except Exception as e:
            health_status["redis"]["status"] = "unhealthy"
            health_status["redis"]["error"] = str(e)
            health_status["status"] = "unhealthy"

    status_code = 200 if health_status["status"] == "healthy" else 503
    return JsonResponse(health_status, status=status_code)
