# Using this file for routing the websocket
# This is the consumer that handles the websocket connection

from django.urls import path
from . import consumers

print("inside routiing")
websocket_urlpatterns=[
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()), # Asynchronous Server Gateway Interface
]