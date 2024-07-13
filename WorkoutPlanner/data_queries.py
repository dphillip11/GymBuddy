import datetime

# project
from .models import Exercise, ExerciseRecord, MuscleGroupTag, Workout, WorkoutRecord
from .data_classes import (
    ActiveWorkoutItemData,
    CalendarItemData,
    ExerciseDetailItemData,
    ExerciseRecordsItemData,
)


def get_active_workout_item_data(exercise_id):
    """
    Construct `ActiveWorkoutItemData` for the given `exercise_id`.

    Args:
        exercise_id (int): The ID of the exercise.

    Returns:
        ActiveWorkoutItemData: The data class instance containing the exercise information and records.
    """
    exercise = Exercise.objects.get(id=exercise_id)
    todays_date = datetime.date.today()
    last_date = ExerciseRecord.objects.filter(exercise=exercise, date__lt=todays_date).order_by('-date').values_list('date', flat=True).first()

    previous_record_item = None

    if last_date:
        previous_record_item = get_exercise_records_item_data( exercise_id,last_date.year, last_date.month, last_date.day )

    todays_record_item = get_exercise_records_item_data( exercise_id,todays_date.year, todays_date.month, todays_date.day )

    return ActiveWorkoutItemData(
        exercise_id=exercise.id,
        name=exercise.name,
        description=exercise.description,
        previous_record_item=previous_record_item,
        todays_record_item=todays_record_item
    )


def get_calendar_item_data(year, month, day):
    """
    Construct `CalendarItemData` for the given date.

    Args:
        year (int): The year of the calendar date.
        month (int): The month of the calendar date.
        day (int): The day of the calendar date.

    Returns:
        CalendarItemData: The data class instance containing the workout entries for the given date.
    """
    workout_records = WorkoutRecord.objects.filter(
        date__year=year, date__month=month, date__day=day
    ).select_related('workout')   

    workout_entries = [workout_record.workout for workout_record in workout_records]

    is_today = (year, month, day) == (datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)
    is_completed = WorkoutRecord.objects.filter(date__year=year, date__month=month, date__day=day, isCompleted=True).exists()

    return CalendarItemData(
        year=year,
        month=month,
        day=day,
        workout_entries=workout_entries,
        is_today=is_today,
        is_completed=is_completed
    )


def get_exercise_detail_item_data(exercise_id):
    """
    Construct `ExerciseDetailItemData` for the given `exercise_id`.

    Args:
        exercise_id (int): The ID of the exercise.

    Returns:
        ExerciseDetailItemData: The data class instance containing details about the exercise.
    """
    try:
        exercise = Exercise.objects.get(id=exercise_id)
        muscle_groups = MuscleGroupTag.objects.filter(exercise=exercise).select_related('muscle_group').values_list('muscle_group__name', flat=True)

        return ExerciseDetailItemData(
            exercise_id=exercise.id,
            name=exercise.name,
            description=exercise.description,
            muscle_groups=list(muscle_groups)
        )
    except:
        return None
    

def get_exercise_records_item_data(exercise_id, year, month, day):
    """
    Construct `ExerciseRecordsItemData` for the given exercise and date.

    Args:
        exercise_id (int): The ID of the exercise.
        year (int): The year of the records.
        month (int): The month of the records.
        day (int): The day of the records.

    Returns:
        ExerciseRecordsItemData: The data class instance containing records for the exercise on the specified date.
    """
    records = list(ExerciseRecord.objects.filter(exercise_id=exercise_id, date__year=year, date__month=month, date__day=day).values('date', 'reps', 'weight'))

    return ExerciseRecordsItemData(
        exercise_id=exercise_id,
        year=year,
        month=month,
        day=day,
        records=records
    )



