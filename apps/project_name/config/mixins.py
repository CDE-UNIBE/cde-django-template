from configurations import values


class DevMixin:
    DEBUG = values.BooleanValue(True)


class ProdMixin:
    DEBUG = values.BooleanValue(False)


class SecurityMixin:
    # Security settings, as recommended from manage.py check --deploy
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = 'DENY'
    # Set the max-age to 12 months
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    # Turn this on as soon as the site is available with ssl.
    # SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
