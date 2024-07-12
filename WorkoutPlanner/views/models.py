from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST

# project
from ..forms import ExerciseForm, ExerciseRecordForm, WorkoutForm, WorkoutRecordForm
from ..models import Exercise, Workout, WorkoutRecord

@require_POST
def create_exercise(request):
    """
    Create a new exercise.
    """
    form = ExerciseForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("Exercise created successfully")
    return HttpResponseBadRequest("Invalid form data")


@require_POST
def create_exercise_record(request):
    """
    Create a new exercise record.
    """
    form = ExerciseRecordForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("Exercise record created successfully")
    return HttpResponseBadRequest("Invalid form data")


@require_POST
def create_workout(request):
    """
    Create a new workout.
    """
    form = WorkoutForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("Workout created successfully")
    return HttpResponseBadRequest("Invalid form data")


@require_POST
def create_workout_record(request):
    """
    Create a new workout record.
    """
    form = WorkoutRecordForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("Workout record created successfully")
    return HttpResponseBadRequest("Invalid form data")


@require_POST
def update_exercise(request, exercise_id):
    """
    Update an existing exercise.
    """
    exercise = get_object_or_404(Exercise, id=exercise_id)
    form = ExerciseForm(request.POST, instance=exercise)
    if form.is_valid():
        form.save()
        return HttpResponse("Exercise updated successfully")
    return HttpResponseBadRequest("Invalid form data")


@require_POST
def update_workout(request, workout_id):
    """
    Update an existing workout.
    """
    workout = get_object_or_404(Workout, id=workout_id)
    form = WorkoutForm(request.POST, instance=workout)
    if form.is_valid():
        form.save()
        return HttpResponse("Workout updated successfully")
    return HttpResponseBadRequest("Invalid form data")


@require_POST
def update_workout_record(request, workout_record_id):
    """
    Update an existing workout record.
    """
    workout_record = get_object_or_404(WorkoutRecord, id=workout_record_id)
    form = WorkoutRecordForm(request.POST, instance=workout_record)
    if form.is_valid():
        form.save()
        return HttpResponse("Workout record updated successfully")
    return HttpResponseBadRequest("Invalid form data")


@require_POST
def delete_exercise(request, exercise_id):
    """
    Delete an existing exercise.
    """
    exercise = get_object_or_404(Exercise, id=exercise_id)
    exercise.delete()
    return HttpResponse("Exercise deleted successfully")


@require_POST
def delete_workout(request, workout_id):
    """
    Delete an existing workout.
    """
    workout = get_object_or_404(Workout, id=workout_id)
    workout.delete()
    return HttpResponse("Workout deleted successfully")


@require_POST
def delete_workout_record(request, workout_record_id):
    """
    Delete an existing workout record.
    """
    workout_record = get_object_or_404(WorkoutRecord, id=workout_record_id)
    workout_record.delete()
    return HttpResponse("Workout record deleted successfully")
