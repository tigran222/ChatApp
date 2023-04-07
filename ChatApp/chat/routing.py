from django.urls import include, path
from chat.consumers import ChatConsumer

websocket_urlpatterns=[
    path('', ChatConsumer.as_asgi()),
]