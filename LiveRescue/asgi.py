"""
ASGI config for LiveRescue project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack  # for authentication
from channels.routing import ProtocolTypeRouter, URLRouter  # for routing
import room.routing 


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LiveRescue.settings')

# This file contains the entry point for the ASGI application.
# The `application` variable represents the ASGI application object.
# It is responsible for handling incoming HTTP requests as well as WebSocket requests and generating responses.
# URLRouter handles routing of websockets to their respective consumers using websocket_urlpatterns defined in routing.py
# AuthMiddlewareStack handles authentication for WebSocket connections
# ProtocolTypeRouter routes incoming requests to their respective handlers based on the protocol type (e.g., HTTP, WebSocket)

print("inside asgi: ")
application = ProtocolTypeRouter({
    "http": get_asgi_application(), # Responsible for handling traditional HTTP requests from Django application
    # This ensures that your traditional Django views and URL routing continue to work as expected, even when you're using Django Channels for WebSocket functionality.
    "websocket": AuthMiddlewareStack(
        URLRouter(
            room.routing.websocket_urlpatterns
        )
    )
})
print("asgi application loaded")

