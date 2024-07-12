from django.urls import path

from WorkoutPlanner import views

# project
from .views.pages import (
    workouts_view, workout_view, exercises_view, calendar_view, gymbuddy_view
)
from .views.components import (
    get_active_workout_item, get_calendar_item, get_workout_detail_item,
    get_exercise_detail_item, get_exercise_records_item
)
from .views.models import (
    create_exercise, create_exercise_record, create_workout, create_workout_record,
    update_exercise, update_workout, update_workout_record,
    delete_exercise, delete_workout, delete_workout_record
)

urlpatterns = [
    # page routes
    path('', workouts_view, name='index'),
    path('calendar/', calendar_view, name='calendar'),
    path('calendar/<int:year>/<int:month>/', calendar_view, name='calendar_with_params'),    path('exercises/', exercises_view, name='exercises'),
    path('gymbuddy/', gymbuddy_view, name='gymbuddy'),
    path('workout/<int:workout_id>/', workout_view, name='workout'),
    path('workouts/', workouts_view, name='workouts'),

    # component routes
    path('get_active_workout_item/<int:exercise_id>', get_active_workout_item, name='get_active_workout_item'),
    path('get_calendar_item/<int:year>/<int:month>/<int:day>/', get_calendar_item, name='get_calendar_item'),
    path('get_exercise_detail_item/<int:exercise_id>', get_exercise_detail_item, name='get_exercise_detail_item'),
    path('get_exercise_records_item/<int:exercise_id>/<int:year>/<int:month>/<int:day>/', get_exercise_records_item, name='get_exercise_records_item'),
    path('get_workout_detail_item/<int:workout_id>', get_workout_detail_item, name='get_workout_detail_item'),

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
