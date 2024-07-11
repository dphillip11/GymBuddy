from django import forms
from .models import Exercise, ExerciseRecord, MuscleGroup, Workout, WorkoutRecord


class ExerciseForm(forms.ModelForm):
    """
    A form for adding new exercises, including the ability to select muscle groups.
    """
    muscle_groups = forms.ModelMultipleChoiceField(
        queryset=MuscleGroup.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Use checkboxes for selecting multiple muscle groups
        required=False,  # This makes the field optional
        help_text='Select the muscle groups targeted by this exercise.'
    )

    class Meta:
        model = Exercise
        fields = ['name', 'description', 'muscle_groups']  # Include muscle_groups in the form fields
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter exercise name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter exercise description', 'rows': 4}),
        }
        labels = {
            'name': 'Exercise Name',
            'description': 'Description',
            'muscle_groups': 'Muscle Groups'
        }


class ExerciseRecordForm(forms.ModelForm):
    """
    A form for adding or updating exercise records.
    """
    class Meta:
        model = ExerciseRecord
        fields = ['exercise', 'reps', 'weight', 'date']


class WorkoutForm(forms.ModelForm):
    """
    A form for adding or updating workouts.
    """
    class Meta:
        model = Workout
        fields = ['name', 'exercises']


class WorkoutRecordForm(forms.ModelForm):
    """
    A form for adding or updating workout records.
    """
    class Meta:
        model = WorkoutRecord
        fields = ['workout', 'date', 'isCompleted']
