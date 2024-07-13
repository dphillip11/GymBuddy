from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model


class Exercise(models.Model):
    """
    Represents an exercise in the workout system.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    muscle_groups = models.ManyToManyField('MuscleGroup', related_name='exercises')  # Direct many-to-many relationship

    def __str__(self):
        return self.name


class ExerciseRecord(models.Model):
    """
    Record of a user's exercise performance.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Using built-in User model
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()
    reps = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.exercise.name} - {self.date}"


class MuscleGroup(models.Model):
    """
    Represents a muscle group for categorizing exercises.
    """
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Workout(models.Model):
    """
    Represents a workout composed of an ordered list of exercises.
    """
    name = models.CharField(max_length=255, blank=False, null=True)
    exercises = models.ManyToManyField('Exercise', related_name='workouts')  # Direct many-to-many relationship

    def __str__(self):
        return self.name


class WorkoutRecord(models.Model):
    """
    Record of a user's completed workout.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Using built-in User model
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.workout.name} - {self.date} - Completed: {self.is_completed}"
