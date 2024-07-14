from django.urls import path

from WorkoutPlanner import views

# project
from .views.pages import (
    metrics_view, workouts_view, workout_view, exercises_view, calendar_view, gymbuddy_view
)

from .views.forms import (
    create_exercise, create_exercise_record, create_workout, create_workout_record,
    update_exercise, update_workout, update_workout_record,
    delete_exercise, delete_workout, delete_workout_record
)

urlpatterns = [
    # page routes
    path('', workouts_view, name='index'),
    path('calendar/', calendar_view, name='calendar'),
    path('calendar/<int:year>/<int:month>/', calendar_view, name='calendar_with_params'),    
    path('exercises/', exercises_view, name='exercises'),
    path('gymbuddy/<int:workout_record_id>', gymbuddy_view, name='gymbuddy'),
    path('metrics/', metrics_view, name='metrics'),
    path('workout/<int:workout_id>/', workout_view, name='workout'),
    path('workouts/', workouts_view, name='workouts'),

    # create models routes
    path('create_exercise/', create_exercise, name='create_exercise'),
    path('create_exercise_record/', create_exercise_record, name='create_exercise_record'),
    path('create_workout/', create_workout, name='create_workout'),
    path('create_workout_record/', create_workout_record, name='create_workout_record'),

    # delete models routes
    path('delete_exercise/<int:exercise_id>/', delete_exercise, name='delete_exercise'),
    path('delete_workout/<int:workout_id>/', delete_workout, name='delete_workout'),
    path('delete_workout_record/<int:workout_record_id>/', delete_workout_record, name='delete_workout_record'),

    # update models routes
    path('update_exercise/<int:exercise_id>/', update_exercise, name='update_exercise'),
    path('update_workout/<int:workout_id>/', update_workout, name='update_workout'),
    path('update_workout_record/<int:workout_record_id>/', update_workout_record, name='update_workout_record'),
]
