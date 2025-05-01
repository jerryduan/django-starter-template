import logging
import time
from uuid import uuid4

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Generate request ID
        request_id = str(uuid4())
        request.request_id = request_id

        # Start timer
        start_time = time.time()

        # Process request
        response = self.get_response(request)

        # Calculate duration
        duration = time.time() - start_time

        # Log request details
        log_data = {
            "request_id": request_id,
            "method": request.method,
            "path": request.path,
            "status_code": response.status_code,
            "duration": round(duration * 1000, 2),  # Convert to milliseconds
            "user": str(request.user) if request.user.is_authenticated else "anonymous",
            "ip": self.get_client_ip(request),
        }

        # Add query parameters if present
        if request.GET:
            log_data["query_params"] = dict(request.GET)

        # Log based on status code
        if response.status_code >= 500:
            logger.error("Request failed", extra=log_data)
        elif response.status_code >= 400:
            logger.warning("Request had issues", extra=log_data)
        else:
            logger.info("Request processed", extra=log_data)

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")
