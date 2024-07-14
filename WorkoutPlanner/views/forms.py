from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.utils import timezone

# project
from WorkoutPlanner.views import components
from ..forms import ExerciseForm, ExerciseRecordForm, WorkoutForm, WorkoutRecordForm
from ..models import Exercise, User, Workout, WorkoutRecord


# Create routes
@require_POST
def create_exercise(request):
    """
    Create a new exercise.
    """
    form = ExerciseForm(request.POST)
    if form.is_valid():
        new_exercise = form.save()

        # apepnd to item list
        components.append_exercise_detail_item(request, new_exercise.id)

        return HttpResponse("Exercise created successfully")
    return HttpResponseBadRequest("Invalid form data")


@require_POST
def create_exercise_record(request):
    """
    Create a new exercise record.
    """
    exercise_id = request.POST.get('exercise_id')
    exercise = get_object_or_404(Exercise, id=exercise_id)
    user = get_object_or_404(User, id=request.user.id)
    date = timezone.now().date()

    form = ExerciseRecordForm(request.POST, exercise_id=exercise_id)
    if form.is_valid():
        exercise_record = form.save(commit=False)
        exercise_record.exercise = exercise
        exercise_record.date = date
        exercise_record.user = user
        exercise_record.save()

        # update item
        components.update_exercise_records_item(request, exercise_id, date.year, date.month, date.day)

        return HttpResponse("Exercise record created successfully")
    return HttpResponseBadRequest("Invalid form data")


@require_POST
def create_workout(request):
    """
    Create a new workout.
    """
    form = WorkoutForm(request.POST)
    if form.is_valid():
        workout = form.save()

        # append item
        components.append_workout_item(request, workout.id)

        return HttpResponse("Workout created successfully")
    return HttpResponseBadRequest("Invalid form data")


@require_POST
def create_workout_record(request):
    """
    Create a new workout record.
    """
    form = WorkoutRecordForm(request.POST)
    if form.is_valid():
        workout_record = form.save(commit=False)
        workout_record.user = request.user
        workout_record.save()

        # update item
        components.update_calendar_item(request, workout_record.date)
        
        return HttpResponse("Workout record created successfully")
    return HttpResponseBadRequest("Invalid form data")


# update routes
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
    workout_record.is_completed = True
    workout_record.date = timezone.datetime.today()
    workout_record.save()
        
    return redirect(reverse("calendar"));


@require_POST
def delete_exercise(request, exercise_id):
    """
    Delete an existing exercise.
    """
    exercise = get_object_or_404(Exercise, id=exercise_id)
    exercise.delete()

    # delete item
    components.delete_exercise_detail(request, exercise_id)

    return HttpResponse("Exercise deleted successfully")


@require_POST
def delete_workout(request, workout_id):
    """
    Delete an existing workout.
    """
    workout = get_object_or_404(Workout, id=workout_id)
    workout.delete()

     # delete item
    components.delete_workout_item(request, workout_id)

    return HttpResponse("Workout deleted successfully")


@require_POST
def delete_workout_record(request, workout_record_id):
    """
    Delete an existing workout record.
    """
    workout_record = get_object_or_404(WorkoutRecord, id=workout_record_id)
    workout_record.delete()
    
    components.delete_workout_record_item(request, workout_record_id)

    return HttpResponse("Workout record deleted successfully")
