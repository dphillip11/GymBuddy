from django.urls import path

from WorkoutPlanner import views
from WorkoutPlanner.constants import *

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
    path(INDEX_URL, workouts_view, name=INDEX_NAME),
    path(CALENDAR_URL, calendar_view, name=CALENDAR_NAME),
    path(CALENDAR_WITH_PARAMS_URL, calendar_view, name=CALENDAR_WITH_PARAMS_NAME),
    path(EXERCISES_URL, exercises_view, name=EXERCISES_NAME),
    path(GYMBUDDY_URL, gymbuddy_view, name=GYMBUDDY_NAME),
    path(WORKOUT_URL, workout_view, name=WORKOUT_NAME),
    path(WORKOUTS_URL, workouts_view, name=WORKOUTS_NAME),

    # create models routes
    path(CREATE_EXERCISE_URL, create_exercise, name=CREATE_EXERCISE_NAME),
    path(CREATE_EXERCISE_RECORD_URL, create_exercise_record, name=CREATE_EXERCISE_RECORD_NAME),
    path(CREATE_WORKOUT_URL, create_workout, name=CREATE_WORKOUT_NAME),
    path(CREATE_WORKOUT_RECORD_URL, create_workout_record, name=CREATE_WORKOUT_RECORD_NAME),

    # delete models routes
    path(DELETE_EXERCISE_URL, delete_exercise, name=DELETE_EXERCISE_NAME),
    path(DELETE_WORKOUT_URL, delete_workout, name=DELETE_WORKOUT_NAME),
    path(DELETE_WORKOUT_RECORD_URL, delete_workout_record, name=DELETE_WORKOUT_RECORD_NAME),

    # update models routes
    path(UPDATE_EXERCISE_URL, update_exercise, name=UPDATE_EXERCISE_NAME),
    path(UPDATE_WORKOUT_URL, update_workout, name=UPDATE_WORKOUT_NAME),
    path(UPDATE_WORKOUT_RECORD_URL, update_workout_record, name=UPDATE_WORKOUT_RECORD_NAME),
]
