from django.urls import path

from WorkoutPlanner import views
from WorkoutPlanner.constants import Constants as C

from .views.pages import (
    workouts_view, workout_view, exercises_view, calendar_view, gymbuddy_view
)

from .views.forms import (
    create_exercise, create_exercise_record, create_workout, create_workout_record,
    update_exercise, update_workout, update_workout_record,
    delete_exercise, delete_workout, delete_workout_record
)

urlpatterns = [
    # page routes
    path(C.INDEX_URL, workouts_view, name=C.INDEX_NAME),
    path(C.CALENDAR_URL, calendar_view, name=C.CALENDAR_NAME),
    path(C.CALENDAR_WITH_PARAMS_URL, calendar_view, name=C.CALENDAR_WITH_PARAMS_NAME),
    path(C.EXERCISES_URL, exercises_view, name=C.EXERCISES_NAME),
    path(C.GYMBUDDY_URL, gymbuddy_view, name=C.GYMBUDDY_NAME),
    path(C.WORKOUT_URL, workout_view, name=C.WORKOUT_NAME),
    path(C.WORKOUTS_URL, workouts_view, name=C.WORKOUTS_NAME),

    # create models routes
    path(C.CREATE_EXERCISE_URL, create_exercise, name=C.CREATE_EXERCISE_NAME),
    path(C.CREATE_EXERCISE_RECORD_URL, create_exercise_record, name=C.CREATE_EXERCISE_RECORD_NAME),
    path(C.CREATE_WORKOUT_URL, create_workout, name=C.CREATE_WORKOUT_NAME),
    path(C.CREATE_WORKOUT_RECORD_URL, create_workout_record, name=C.CREATE_WORKOUT_RECORD_NAME),

    # delete models routes
    path(C.DELETE_EXERCISE_URL, delete_exercise, name=C.DELETE_EXERCISE_NAME),
    path(C.DELETE_WORKOUT_URL, delete_workout, name=C.DELETE_WORKOUT_NAME),
    path(C.DELETE_WORKOUT_RECORD_URL, delete_workout_record, name=C.DELETE_WORKOUT_RECORD_NAME),

    # update models routes
    path(C.UPDATE_EXERCISE_URL, update_exercise, name=C.UPDATE_EXERCISE_NAME),
    path(C.UPDATE_WORKOUT_URL, update_workout, name=C.UPDATE_WORKOUT_NAME),
    path(C.UPDATE_WORKOUT_RECORD_URL, update_workout_record, name=C.UPDATE_WORKOUT_RECORD_NAME),
]
