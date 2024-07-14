import json
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date
from WorkoutPlanner.models import MuscleGroup, Exercise, Workout, ExerciseRecord, WorkoutRecord
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    """
    Custom Django management command to populate the database with dummy data from a JSON file.
    """

    help = 'Populate the database with dummy data from a JSON file'

    def handle(self, *args, **kwargs):
        """
        Load dummy data from 'dummy_data.json' and populate the database.
        """

        # Clear the database
        self.stdout.write(self.style.WARNING('Clearing the database...'))
        WorkoutRecord.objects.all().delete()
        ExerciseRecord.objects.all().delete()
        Workout.objects.all().delete()
        Exercise.objects.all().delete()
        MuscleGroup.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()  # Optionally keep superuser

        self.stdout.write(self.style.SUCCESS('Database cleared.'))

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
            if 'muscle_groups' in exercise_data:
                exercise.muscle_groups.set(
                    [muscle_group_dict[group_name] for group_name in exercise_data['muscle_groups']]
                )
            exercise_dict[exercise_data['name']] = exercise

        # Populate workouts
        for workout_data in data['workouts']:
            workout, created = Workout.objects.get_or_create(name=workout_data['name'])
            exercises_to_add = []
            for exercise_data in workout_data.get('exercises', []):
                exercise = exercise_dict.get(exercise_data['name'])
                if exercise:
                    exercises_to_add.append(exercise)
                else:
                    self.stdout.write(self.style.ERROR(f"Exercise '{exercise_data['name']}' not found for Workout '{workout_data['name']}'"))
            workout.exercises.set(exercises_to_add)

        # Populate users
        user_dict = {}
        for user_data in data['users']:
            user, created = User.objects.get_or_create(
                id=user_data['id'],
                defaults={
                    'username': f'user{user_data["id"]}',  # Example username, change as needed
                    'email': f'user{user_data["id"]}@example.com',  # Example email, change as needed
                    'password': 'password'  # Example password, change as needed
                }
            )
            user_dict[user_data['id']] = user

        # Populate exercise records
        for record_data in data['exercise_records']:
            exercise = exercise_dict.get(record_data['exercise_name'])
            if exercise:
                user = user_dict.get(record_data['user'], User.objects.first())
                ExerciseRecord.objects.create(
                    user=user,
                    exercise=exercise,
                    date=parse_date(record_data['date']),
                    weight=record_data['weight'],
                    reps=record_data['reps']
                )
            else:
                self.stdout.write(self.style.ERROR(f"Exercise '{record_data['exercise_name']}' not found for ExerciseRecord"))

        # Populate workout records and mark as completed if the date is before today
        today = parse_date('2024-07-14')  # Use a fixed date for testing or replace with datetime.date.today() for the current date
        for record_data in data['workout_records']:
            workout = Workout.objects.filter(id=record_data['workout_id']).first() or Workout.objects.first()
            user = user_dict.get(record_data['user'], User.objects.first())
            if workout and user:
                is_completed = parse_date(record_data['date']) < today
                WorkoutRecord.objects.create(
                    user=user,
                    workout=workout,
                    date=parse_date(record_data['date']),
                    is_completed=is_completed
                )
            else:
                self.stdout.write(self.style.ERROR(f"Workout with ID '{record_data['workout_id']}' or User with ID '{record_data['user']}' not found for WorkoutRecord"))

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy data'))
