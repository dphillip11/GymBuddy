from django.contrib import admin
from .models import Exercise, ExerciseRecord, MuscleGroup, Workout, WorkoutRecord

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class ExerciseRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'exercise', 'date', 'weight', 'reps')
    list_filter = ('date', 'user', 'exercise')
    search_fields = ('exercise__name', 'user__username')

class MuscleGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class WorkoutRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'workout', 'date', 'is_completed')
    list_filter = ('date', 'user', 'workout', 'is_completed')
    search_fields = ('workout__name', 'user__username')

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(ExerciseRecord, ExerciseRecordAdmin)
admin.site.register(MuscleGroup, MuscleGroupAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(WorkoutRecord, WorkoutRecordAdmin)
