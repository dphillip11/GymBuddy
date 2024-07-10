# Libraries
from datetime import date, timedelta
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
import calendar

# Project
from .forms import ExerciseForm
from .models import MuscleGroup, MuscleGroupTag, Exercise, Workout, User, WorkoutCalendarEntry, ExerciseRecord, WorkoutRecord
from .data_classes import ExerciseData, WorkoutDetailData, WorkoutHistory
from .forms import ExerciseForm


def workout_list(request):
    """
    View to list all workouts.
    """
    workouts = Workout.objects.all()
    context = {
        'workouts': workouts
    }
    return render(request, 'workoutplanner/workout_list.html', context)


def workout_detail(request, workout_id):
    """
    View function for displaying the details of a workout.
    """
    workout = get_object_or_404(Workout, id=workout_id)
    exercises = workout.exercises.all().order_by('workoutexercise__order')  # Get exercises ordered by their defined order in the workout

    exercises_data = []
    for exercise in exercises:
        muscle_groups = MuscleGroupTag.objects.filter(exercise=exercise).select_related('muscle_group')
        muscle_group_names = [tag.muscle_group.name for tag in muscle_groups]
        exercises_data.append(ExerciseData(exercise=exercise, muscle_groups=muscle_group_names))

    workout_data = WorkoutDetailData(workout=workout, exercises_data=exercises_data)

    context = {
        'workout_data': workout_data
    }

    return render(request, 'workoutplanner/workout_detail.html', context)


def exercise_list(request):
    """View function for listing all exercises."""
    exercises = Exercise.objects.all()

    exercises_data = []
    for exercise in exercises:
        muscle_groups = MuscleGroupTag.objects.filter(exercise=exercise).select_related('muscle_group')
        muscle_group_names = [tag.muscle_group.name for tag in muscle_groups]
        exercises_data.append(ExerciseData(exercise=exercise, muscle_groups=muscle_group_names))

    form = ExerciseForm()

    context = {
        'exercises_data': exercises_data,
        'form':form,
    }
    return render(request, 'workoutplanner/exercise_list.html', context)


def add_exercise(request):
    """
    View to add a new exercise.
    """
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save()  # Save the exercise instance
            # Add tags for selected muscle groups
            muscle_groups = form.cleaned_data['muscle_groups']
            for muscle_group in muscle_groups:
                MuscleGroupTag.objects.get_or_create(
                    exercise=exercise,
                    muscle_group=muscle_group
                )
            print(exercise)
            print(muscle_groups)
    
    return redirect('exercise_list')


def calendar_view(request, year=None, month=None):
    today = date.today()

    if year is None or month is None:
        year = today.year
        month = today.month

    # Calculate previous and next month
    first_day_of_month = date(year, month, 1)
    last_day_of_month = calendar.monthrange(year, month)[1]

    previous_month_date = first_day_of_month - timedelta(days=1)
    next_month_date = first_day_of_month + timedelta(days=last_day_of_month)

    context = {
        'month': month,
        'year': year,
        'month_name': calendar.month_name[month],
        'days': range(1, last_day_of_month + 1),
        'previous_year': previous_month_date.year,
        'previous_month': previous_month_date.month,
        'next_year': next_month_date.year,
        'next_month': next_month_date.month
    }

    return render(request, 'workoutplanner/calendar.html', context)


def calendar_item_view(request, year, month, day):
    item_date = date(year, month, day)
    today = date.today()
    workouts = Workout.objects.all()
    workout_record = WorkoutRecord.objects.filter(date=item_date).first()

    workout_history = None
    is_completed = False
    is_today = False
    is_future = False

    if workout_record:
        is_completed = True
        workout_history = workout_record
    else:
        workout_history = WorkoutHistory(
            workout=Workout(name="No workout assigned"),
            is_completed=False,
            is_today=(item_date == today),
            is_future=(item_date > today)
        )
    
    context = {
        'day': day,
        'month': month,
        'year': year,
        'workout_history': workout_history,
        'workouts': workouts,
        'is_completed': is_completed,
        'is_today': item_date == today,
        'is_future': item_date > today,
    }

    return render(request, 'workoutplanner/calendar_item.html', context)