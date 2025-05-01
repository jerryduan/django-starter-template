import logging
import time
import functools
from typing import Callable

logger = logging.getLogger(__name__)


def monitor_performance(view_func: Callable) -> Callable:
    """
    Decorator to monitor view performance and log metrics.
    Usage:
        @monitor_performance
        def my_view(request):
            ...
    """

    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        start_time = time.time()

        try:
            response = view_func(request, *args, **kwargs)
            status_code = response.status_code
            error = None
        except Exception as e:
            status_code = 500
            error = str(e)
            raise
        finally:
            duration = time.time() - start_time

            # Log performance metrics
            log_data = {
                "view": view_func.__name__,
                "duration": round(duration * 1000, 2),  # Convert to milliseconds
                "status_code": status_code,
                "request_id": getattr(request, "request_id", "unknown"),
            }

            if error:
                log_data["error"] = error
                logger.error("View performance", extra=log_data)
            elif status_code >= 500:
                logger.error("View performance", extra=log_data)
            elif status_code >= 400:
                logger.warning("View performance", extra=log_data)
            else:
                logger.info("View performance", extra=log_data)

        return response

    return wrapper
