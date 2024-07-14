import datetime
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
import calendar

# project
from WorkoutPlanner.data_queries import get_active_workout_item_data, get_calendar_item_data, get_exercise_detail_item_data
from WorkoutPlanner.forms import ExerciseForm, ExerciseRecordForm, WorkoutForm, WorkoutRecordForm
from WorkoutPlanner.models import Exercise, MuscleGroup, Workout, WorkoutRecord

def calendar_view(request, year=None, month=None):
    """
    Display the calendar view.
    """
    # Get the current date if year and month are not provided
    if not year or not month:
        today = timezone.now()
        year = year or today.year
        month = month or today.month

    num_days = calendar.monthrange(year, month)[1]
    calendar_items = [
        get_calendar_item_data(datetime.date(year, month, day))
        for day in range(1, num_days + 1)
    ]

    # Calculate the previous and next month
    next_month = month + 1
    next_year = year
    if next_month > 12:
        next_month = 1
        next_year += 1

    prev_month = month - 1
    prev_year = year
    if prev_month < 1:
        prev_month = 12
        prev_year -= 1

    context = {
        'year': year,
        'month': month,
        'calendar_items': calendar_items,
        'form': WorkoutRecordForm(),
        'next_month_url': reverse('calendar_with_params', kwargs={'year': next_year, 'month': next_month}),
        'prev_month_url': reverse('calendar_with_params', kwargs={'year': prev_year, 'month': prev_month}),
    }
    
    return render(request, 'workoutplanner/pages/calendar_page.html', context)


def exercises_view(request):
    """
    Display the list of exercises.
    """
    items = [
        get_exercise_detail_item_data(exercise.id)
        for exercise in Exercise.objects.all()
    ]

    context = {
        'items':items,
        'form': ExerciseForm(),
        'form_name':"Create Exercise",
        'form_action':reverse('create_exercise')
    }

    return render(request, 'workoutplanner/pages/exercises_page.html', context )


def gymbuddy_view(request, workout_record_id):
    """
    Display the gymbuddy page and perform a workout.
    
    Args:
        request (HttpRequest): The request object.
        workout_id (int): The ID of the workout to display.
    
    Returns:
        HttpResponse: The rendered gymbuddy page with workout details.
    """
    workout_record = get_object_or_404(WorkoutRecord, id=workout_record_id)

    items = [
        get_active_workout_item_data(exercise.id)
        for exercise in workout_record.workout.exercises.all()
    ]

    context = {
        'workout_record': workout_record,
        'active_workout_items': items,
        'form':ExerciseRecordForm(),
        'workout_record_form':WorkoutRecordForm()
    }

    return render(request, 'workoutplanner/pages/gymbuddy_page.html', context )


def metrics_view(request):
    """
    Display graphs and metrics about exercise history
    """
    exercises = Exercise.objects.all()
    muscle_groups = MuscleGroup.objects.all()
    
    context = {
        'exercises': exercises,
        'muscle_groups': muscle_groups,
    }
    
    return render(request, 'workoutplanner/pages/metrics_page.html', context)


def workout_view(request, workout_id):
    """
    Display a specific workout.
    """
    workout = get_object_or_404(Workout, id=workout_id)

    exercise_items = [
        get_exercise_detail_item_data(exercise.id)
        for exercise in workout.exercises.all()
    ]

    context = {
        'workout': workout,
        'exercise_items':exercise_items,
    }
    
    # Render the 'workout_page.html' template with the context data
    return render(request, 'workoutplanner/pages/workout_page.html', context)


def workouts_view(request):
    """
    Display the workouts.
    """
    context = {
        'workouts':Workout.objects.all(),
        'form': WorkoutForm(),
        'form_name':"Create Workout",
        'form_action':reverse('create_workout')
    }
    return render(request, 'workoutplanner/pages/workouts_page.html', context )
