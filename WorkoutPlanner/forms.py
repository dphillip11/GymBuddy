from django import forms
from .models import Exercise, ExerciseRecord, MuscleGroup, Workout, WorkoutRecord


class ExerciseForm(forms.ModelForm):
    """
    A form for adding new exercises, including the ability to select muscle groups.
    """
    muscle_groups = forms.ModelMultipleChoiceField(
        queryset=MuscleGroup.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False, 
    )

    class Meta:
        model = Exercise
        fields = ['name', 'description', 'muscle_groups']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter exercise name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter exercise description', 'rows': 2}),
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
        fields = ['reps', 'weight']
    
    def __init__(self, *args, **kwargs):
        self.exercise_id = kwargs.pop('exercise_id', None)
        super().__init__(*args, **kwargs)


class WorkoutForm(forms.ModelForm):
    """
    A form for adding or updating workouts.
    """
    exercises = forms.ModelMultipleChoiceField(
        queryset=Exercise.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

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
