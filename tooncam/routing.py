from django.urls import path
from tooncam.video.consumers import VideoConsumer

websocket_urlpatterns = [
    path('ws/video/', VideoConsumer.as_asgi()),
]
