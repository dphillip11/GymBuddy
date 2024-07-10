from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import MuscleGroup, Exercise, Workout, User, WorkoutCalendarEntry, ExerciseRecord, WorkoutRecord
