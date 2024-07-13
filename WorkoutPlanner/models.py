from django.db import models


class User(models.Model):
    """
    Represents a user of the GymBuddy application.
    """
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"User {self.id}"
    

class Exercise(models.Model):
    """
    Represents an exercise in the workout system.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class ExerciseRecord(models.Model):
    """
    Record of a user's exercise performance.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()
    reps = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user} - {self.exercise.name} - {self.date}"


class MuscleGroup(models.Model):
    """
    Represents a muscle group for categorizing exercises.
    """
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class MuscleGroupTag(models.Model):
    """
    Tags to categorize exercises by muscle groups.
    """
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE, related_name='muscle_group_tags')
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('exercise', 'muscle_group')  # Ensure unique tag for each exercise and muscle group combination.

    def __str__(self):
        return f"{self.exercise.name} - {self.muscle_group.name}"

    

class Workout(models.Model):
    """
    Represents a workout composed of an ordered list of exercises.
    """
    name = models.CharField(max_length=255, blank=False, null=True)
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')

    def __str__(self):
        return self.name


class WorkoutExercise(models.Model):
    """
    Through model for Workout and Exercise to maintain order of exercises.
    """
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.workout.id} - {self.exercise.name} ({self.order})"


class WorkoutRecord(models.Model):
    """
    Record of a user's completed workout.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date = models.DateField()
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.workout.id} - {self.date} - Completed: {self.isCompleted}"
