import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'botgi_crm.settings')
from botgi_crm import django_compat  # noqa: F401

# 1. Initialize Django ASGI application FIRST
django_asgi_app = get_asgi_application()

# 2. Import channels and routing AFTER Django is initialized
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from job_tickets import routing

application = ProtocolTypeRouter({
    # HTTP requests handled by Django ASGI
    "http": django_asgi_app,

    # WebSocket connections handled by Channels
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
