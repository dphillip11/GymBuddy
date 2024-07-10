# Generated by Django 5.0.7 on 2024-07-10 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Exercise",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="MuscleGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="Workout",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExerciseRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("weight", models.FloatField()),
                ("reps", models.PositiveIntegerField()),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="WorkoutPlanner.exercise",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="WorkoutPlanner.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WorkoutCalendarEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="WorkoutPlanner.user",
                    ),
                ),
                (
                    "workout",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="WorkoutPlanner.workout",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WorkoutExercise",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.PositiveIntegerField()),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="WorkoutPlanner.exercise",
                    ),
                ),
                (
                    "workout",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="WorkoutPlanner.workout",
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
            },
        ),
        migrations.AddField(
            model_name="workout",
            name="exercises",
            field=models.ManyToManyField(
                through="WorkoutPlanner.WorkoutExercise", to="WorkoutPlanner.exercise"
            ),
        ),
        migrations.CreateModel(
            name="WorkoutRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="WorkoutPlanner.user",
                    ),
                ),
                (
                    "workout",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="WorkoutPlanner.workout",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MuscleGroupTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="muscle_group_tags",
                        to="WorkoutPlanner.exercise",
                    ),
                ),
                (
                    "muscle_group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="WorkoutPlanner.musclegroup",
                    ),
                ),
            ],
            options={
                "unique_together": {("exercise", "muscle_group")},
            },
        ),
    ]
