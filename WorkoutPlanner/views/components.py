from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


from ..data_queries import (
    get_active_workout_item_data,
    get_calendar_item_data,
    get_exercise_detail_item_data,
    get_exercise_records_item_data,
)

# Called by forms on save
def send_update_to_websocket(element_id, new_content, append=False):
    channel_layer = get_channel_layer()
    if channel_layer is None:
        raise RuntimeError('Channel Layer not configured properly.')
    async_to_sync(channel_layer.group_send)(
        'update_group', 
        {
            'type': 'update_message',
            'element_id': element_id,
            'new_content': new_content,
            'append':append
        }
    )


# Generic update function
def update_item(template_name, context_data, element_id):
    context = context_data
    new_content = render_to_string(template_name, context)
    send_update_to_websocket(element_id, new_content)


# Specific update functions using the generic update function
def update_active_workout_item(exercise_id):
    context_data = {'item': get_active_workout_item_data(exercise_id)}
    element_id = f'active_workout_item_{exercise_id}'
    update_item('workoutplanner/components/active_workout_item.html', context_data, element_id)


def update_calendar_item(year, month, day):
    context_data = {'item': get_calendar_item_data(year, month, day)}
    element_id = f'calendar_item_{year}_{month}_{day}'
    update_item('workoutplanner/components/calendar_item.html', context_data, element_id)


def update_exercise_detail_item(exercise_id):
    context_data = {'item': get_exercise_detail_item_data(exercise_id)}
    element_id = f'exercise_detail_item_{exercise_id}'
    update_item('workoutplanner/components/exercise_detail_item.html', context_data, element_id)


def update_exercise_records_item(exercise_id, year, month, day):
    context_data = {'item': get_exercise_records_item_data(exercise_id, year, month, day)}
    element_id = f'exercise_records_item_{exercise_id}_{year}_{month}_{day}'
    update_item('workoutplanner/components/exercise_records_item.html', context_data, element_id)