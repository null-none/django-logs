from django.utils.decorators import decorator_from_middleware

from logs.middleware import UserLoggingMiddleware

log_current_user = decorator_from_middleware(UserLoggingMiddleware)
