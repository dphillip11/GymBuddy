from django.contrib import admin
from .models import MuscleGroup, MuscleGroupTag, Exercise, Workout, WorkoutExercise, User, ExerciseRecord, WorkoutRecord

class MuscleGroupTagInline(admin.TabularInline):
    model = MuscleGroupTag
    extra = 1


class ExerciseAdmin(admin.ModelAdmin):
    """
    Admin interface for managing exercises.
    """
    list_display = ('name', 'description')
    inlines = [MuscleGroupTagInline]


class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1


class WorkoutAdmin(admin.ModelAdmin):
    """
    Admin interface for managing workouts.
    """
    list_display = ('id',)
    inlines = [WorkoutExerciseInline]


class UserAdmin(admin.ModelAdmin):
    """
    Admin interface for managing users.
    """
    list_display = ('id',)


class ExerciseRecordAdmin(admin.ModelAdmin):
    """
    Admin interface for managing exercise records.
    """
    list_display = ('user', 'exercise', 'date', 'weight', 'reps')


class WorkoutRecordAdmin(admin.ModelAdmin):
    """
    Admin interface for managing workout records.
    """
    list_display = ('user', 'workout', 'date', 'isCompleted')

admin.site.register(MuscleGroup)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(ExerciseRecord, ExerciseRecordAdmin)
admin.site.register(WorkoutRecord, WorkoutRecordAdmin)
