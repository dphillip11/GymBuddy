from django.shortcuts import render


def calendar_view(request):
    """
    Display the calendar view.
    """
    return render(request, 'workoutplanner/pages/calendar_page.html')


def exercises_view(request):
    """
    Display the list of exercises.
    """
    return render(request, 'workoutplanner/pages/exercises_page.html')


def gymbuddy_view(request):
    """
    Display the gymbuddy page and do a workout.
    """
    return render(request, 'workoutplanner/pages/gymbuddy_page.html')


def workout_view(request, workout_id):
    """
    Display a specific workout.
    """
    return render(request, 'workoutplanner/pages/workout_page.html', {'workout_id': workout_id})


def workouts_view(request):
    """
    Display the workouts.
    """
    return render(request, 'workoutplanner/pages/workouts_page.html')
