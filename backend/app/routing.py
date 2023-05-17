from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from app.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'^ws/(?P<room_name>[^/]+)/$', ChatConsumer.as_asgi())
]
