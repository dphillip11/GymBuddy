from dataclasses import dataclass
import datetime
from typing import Optional, List


# Data Class for `get_active_workout_item`
@dataclass
class ActiveWorkoutItemData:
    exercise_id: int
    name: str
    description: str
    previous_record_item: Optional[dict] = None
    todays_record_item: Optional[dict] = None


# Data Class for `get_calendar_item`
@dataclass
class CalendarItemData:
    date : datetime.date
    workout_records: List[dict]
    is_today: Optional[bool] = None
    is_completed: Optional[bool] = None
    

# Data Class for `get_exercise_records_item`
@dataclass
class ExerciseRecordsItemData:
    exercise_id: int
    year: int
    month: int
    day: int
    records: List[dict]  # List of records for the exercise on this date