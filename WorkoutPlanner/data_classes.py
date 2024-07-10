# myapp/data_classes.py

from dataclasses import dataclass
from typing import List

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
