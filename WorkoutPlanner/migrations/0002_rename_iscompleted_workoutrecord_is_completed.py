# Generated by Django 5.0.6 on 2024-07-13 18:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("WorkoutPlanner", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="workoutrecord",
            old_name="isCompleted",
            new_name="is_completed",
        ),
    ]