from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'update_items/$', consumers.UpdateItemsConsumer.as_asgi(), name='update_items'),
    re_path(r'metrics/$', consumers.ExerciseRecordConsumer.as_asgi(), name='metrics'),
]
