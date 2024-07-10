from django.urls import path
from . import views

# app_name = 'workoutplanner'

urlpatterns = [
    path('', views.workout_list, name='index'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('workouts/<int:workout_id>/', views.workout_detail, name='workout_detail'),
    path('exercises/', views.exercise_list, name='exercise_list'), 
    path('add-exercise/', views.add_exercise, name='add_exercise'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('calendar/<int:year>/<int:month>/', views.calendar_view, name='calendar'),  # Calendar view with month/year
    path('calendar-item/<int:year>/<int:month>/<int:day>/', views.calendar_item_view, name='calendar_item'),
]