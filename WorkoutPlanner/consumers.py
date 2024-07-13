# workoutplanner/consumers.py

from channels.generic.websocket import AsyncWebsocketConsumer
import json

class UpdateItemsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join the update group
        await self.channel_layer.group_add(
            "update_group",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the update group
        await self.channel_layer.group_discard(
            "update_group",
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle the WebSocket message
        pass

    # Handler for the `update_message` type
    async def update_message(self, event):
        element_id = event['element_id']
        new_content = event['new_content']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'element_id': element_id,
            'new_content': new_content
        }))
