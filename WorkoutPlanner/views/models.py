from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

# project
from ..forms import ExerciseForm, ExerciseRecordForm, WorkoutForm, WorkoutRecordForm


def create_exercise(request):
    """
    Create a new exercise.
    """
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm()
    return render(request, 'workoutplanner/forms/generic_form.html', {'form': form})


def create_exercise_record(request):
    """
    Create a new exercise record.
    """
    if request.method == 'POST':
        form = ExerciseRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')  # Redirect to a suitable page
    else:
        form = ExerciseRecordForm()
    return render(request, 'workoutplanner/forms/generic_form.html', {'form': form})


def create_workout(request):
    """
    Create a new workout.
    """
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workouts')
    else:
        form = WorkoutForm()
    return render(request, 'workoutplanner/forms/generic_form.html', {'form': form})


def create_workout_record(request):
    """
    Create a new workout record.
    """
    if request.method == 'POST':
        form = WorkoutRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')  # Redirect to a suitable page
    else:
        form = WorkoutRecordForm()
    return render(request, 'workoutplanner/forms/generic_form.html', {'form': form})


def update_exercise(request, exercise_id):
    """
    Update an existing exercise.
    """
    exercise = get_object_or_404(Exercise, id=exercise_id)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'workoutplanner/forms/generic_form.html', {'form': form})


def update_workout(request, workout_id):
    """
    Update an existing workout.
    """
    workout = get_object_or_404(Workout, id=workout_id)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workouts')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'workoutplanner/forms/generic_form.html', {'form': form})


def update_workout_record(request, workout_record_id):
    """
    Update an existing workout record.
    """
    workout_record = get_object_or_404(WorkoutRecord, id=workout_record_id)
    if request.method == 'POST':
        form = WorkoutRecordForm(request.POST, instance=workout_record)
        if form.is_valid():
            form.save()
            return redirect('calendar')  # Redirect to a suitable page
    else:
        form = WorkoutRecordForm(instance=workout_record)
    return render(request, 'workoutplanner/forms/generic_form.html', {'form': form})


def delete_exercise(request, exercise_id):
    """
    Delete an existing exercise.
    """
    exercise = get_object_or_404(Exercise, id=exercise_id)
    exercise.delete()
    return redirect('exercise_list')


def delete_workout(request, workout_id):
    """
    Delete an existing workout.
    """
    workout = get_object_or_404(Workout, id=workout_id)
    workout.delete()
    return redirect('workouts')


def delete_workout_record(request, workout_record_id):
    """
    Delete an existing workout record.
    """
    workout_record = get_object_or_404(WorkoutRecord, id=workout_record_id)
    workout_record.delete()
    return redirect('calendar')
