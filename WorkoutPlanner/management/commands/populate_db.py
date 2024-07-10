import json
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date
from WorkoutPlanner.models import MuscleGroup, MuscleGroupTag, Exercise, Workout, WorkoutExercise, User, WorkoutCalendarEntry, ExerciseRecord, WorkoutRecord

class Command(BaseCommand):
    """
    Custom Django management command to populate the database with dummy data from a JSON file.
    """

    help = 'Populate the database with dummy data from a JSON file'

    def handle(self, *args, **kwargs):
        """
        Load dummy data from 'dummy_data.json' and populate the database.
        """
        # Open the JSON file
        with open('dummy_data.json') as f:
            data = json.load(f)

        # Populate muscle groups
        muscle_group_dict = {}
        for group_name in data['muscle_groups']:
            muscle_group, created = MuscleGroup.objects.get_or_create(name=group_name)
            muscle_group_dict[group_name] = muscle_group

        # Populate exercises
        exercise_dict = {}
        for exercise_data in data['exercises']:
            exercise, created = Exercise.objects.get_or_create(
                name=exercise_data['name'],
                defaults={'description': exercise_data['description']}
            )
            for muscle_group_name in exercise_data['muscle_groups']:
                MuscleGroupTag.objects.get_or_create(
                    exercise=exercise,
                    muscle_group=muscle_group_dict[muscle_group_name]
                )
            exercise_dict[exercise_data['name']] = exercise

        # Populate workouts
        for workout_data in data['workouts']:
            workout, created = Workout.objects.get_or_create(name=workout_data['name'])
            for exercise_info in workout_data['exercises']:
                exercise = exercise_dict[exercise_info['name']]
                WorkoutExercise.objects.create(
                    workout=workout,
                    exercise=exercise,
                    order=exercise_info['order']
                )

        # Populate users
        user_dict = {}
        for user_data in data['users']:
            user, created = User.objects.get_or_create(id=user_data['id'])
            user.save()
            user_dict[user_data['id']] = user

        # Populate workout calendar entries
        for entry_data in data['workout_calendar_entries']:
            WorkoutCalendarEntry.objects.create(
                user=user_dict[entry_data['user']],
                date=parse_date(entry_data['date']),
                workout_id=entry_data['workout_id']
            )

        # Populate exercise records
        for record_data in data['exercise_records']:
            ExerciseRecord.objects.create(
                user=user_dict[record_data['user']],
                exercise=exercise_dict[record_data['exercise_name']],
                date=parse_date(record_data['date']),
                weight=record_data['weight'],
                reps=record_data['reps']
            )

        # Populate workout records
        for record_data in data['workout_records']:
            WorkoutRecord.objects.create(
                user=user_dict[record_data['user']],
                workout_id=record_data['workout_id'],
                date=parse_date(record_data['date'])
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy data'))
