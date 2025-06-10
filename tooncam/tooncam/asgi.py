"""ASGI config for tooncam project with Channels support."""
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tooncam.settings')
django_asgi_app = get_asgi_application()

import tooncam.routing

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': URLRouter(tooncam.routing.websocket_urlpatterns),
})
