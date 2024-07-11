# myapp/data_classes.py

from dataclasses import dataclass
from typing import List
from datetime import date
from .models import Workout, Exercise, ExerciseRecord

@dataclass
class ExerciseData:
    """
    Data class for holding exercise information and associated muscle groups.
    """
    exercise: 'Exercise'
    muscle_groups: List[str]

@dataclass
class WorkoutDetailData:
    """
    Data class for holding workout information and associated exercises data.
    """
    workout: 'Workout'
    exercises_data: List[ExerciseData]

@dataclass
class WorkoutHistory:
    workout: Workout
    is_completed: bool
    is_today: bool
    is_future: bool

@dataclass
class WorkoutItem:
    """
    Data class for holding workout information for a single exercise.
    """
    exercise: 'Exercise'
    previous_exercise_records: List['ExerciseRecord']
    todays_exercise_records: List['ExerciseRecord']

