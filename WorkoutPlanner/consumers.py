from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
import json

# project
from WorkoutPlanner.views.metrics import fetch_exercise_records


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
        append = event['append']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'element_id': element_id,
            'new_content': new_content,
            'append': append
        }))


class ExerciseRecordConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        data = json.loads(text_data)
        exercise_id = data.get('exercise_id')
        muscle_group_id = data.get('muscle_group_id')
        metric = data.get('metric')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        records = fetch_exercise_records(exercise_id, muscle_group_id, metric, start_date, end_date)

        self.send(text_data=json.dumps(records))
