from django.urls import path
from . import views

# app_name = 'workoutplanner'

urlpatterns = [
    path('', views.workout_list, name='index'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('workouts/<int:workout_id>/', views.workout_detail, name='workout_detail'),
    path('exercises/', views.exercise_list, name='exercise_list'),    
    path('calendar/', views.calendar_view, name='calendar-view'),
]