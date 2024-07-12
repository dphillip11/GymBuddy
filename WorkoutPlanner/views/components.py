from django.http import JsonResponse


from ..data_queries import (
    get_active_workout_item_data,
    get_calendar_item_data,
    get_exercise_detail_item_data,
    get_exercise_records_item_data,
)


def get_active_workout_item(request, exercise_id):
    data = get_active_workout_item_data(exercise_id)
    return JsonResponse(data.__dict__)


def get_calendar_item(request, year, month, day):
    data = get_calendar_item_data(year, month, day)
    return JsonResponse(data.__dict__)


def get_exercise_detail_item(request, exercise_id):
    data = get_exercise_detail_item_data(exercise_id)
    return JsonResponse(data.__dict__)


def get_exercise_records_item(request, exercise_id, year, month, day):
    data = get_exercise_records_item_data(exercise_id, year, month, day)
    return JsonResponse(data.__dict__)