from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from .models import MuscleGroup, MuscleGroupTag, Exercise, Workout, User, WorkoutCalendarEntry, ExerciseRecord, WorkoutRecord
from .data_classes import ExerciseData, WorkoutDetailData

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

    context = {
        'exercises_data': exercises_data,
    }
    return render(request, 'workoutplanner/exercise_list.html', context)


def calendar_view(request):
    return render(request, 'workoutplanner/calendar.html') 