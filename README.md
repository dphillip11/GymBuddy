# GymBuddy
A basic demonstration of a project using Django to help you at the gym

Use the initial_setup.sh file to get started.

# Django Project Route Documentation

This document provides a detailed list of all routes used in the Django project. Each route is listed with its URL pattern, associated view, and name. This is useful for understanding the available endpoints and their functionalities.

## Table of Contents

- [Architecture](#architecture)
- [Page Routes](#page-routes)
- [Model Creation Routes](#model-creation-routes)
- [Model Deletion Routes](#model-deletion-routes)
- [Model Update Routes](#model-update-routes)

---

## Architecture

[Diagram](docs/GymBuddyLayout.pdf)

The application is designed to manage workout plans, exercises, and records with a focus on dynamic, server-authoritative updates using WebSockets. The architecture is organized into three main components:

1. **Forms** - Responsible for editing models.
2. **Data Queries** - Responsible for querying models and providing views with data.
3. **Component Views** - Triggered by WebSocket connections to dynamically update individual elements on the page.

## 1. Forms

### Role

Forms are used to handle the creation, updating, and deletion of models. They provide the user interface for data entry and are directly linked to Django’s model layer to perform CRUD (Create, Read, Update, Delete) operations.

## 2. Data Queries

### Role

Data queries are responsible for retrieving data from the database. They provide the necessary data to views and templates through data classes and query functions.

## 3. Component Views

### Role

Component views are triggered by WebSocket connections. They handle dynamic updates of individual elements on the page without requiring a full page reload. This approach allows for server-side authority and reduces the coupling between models and page updates.

---

## Page Routes

These routes are used to render various pages of the application.

| **URL Pattern**                             | **View**            | **Name**                  | **Description**                     |
|----------------------------------------------|---------------------|---------------------------|-------------------------------------|
| `/`                                          | `workouts_view`     | `index`                   | Home page (index view)             |
| `calendar/`                                 | `calendar_view`     | `calendar`                | Calendar view (no params)          |
| `calendar/<int:year>/<int:month>/`         | `calendar_view`     | `calendar_with_params`   | Calendar view with year and month params |
| `exercises/`                                | `exercises_view`    | `exercises`               | Exercises view                      |
| `gymbuddy/<int:workout_id>`                 | `gymbuddy_view`     | `gymbuddy`                | Gym buddy view for a specific workout |
| `metrics/`                                  | `metrics`           | `metrics`                 | Exercise metrics                    |
| `workout/<int:workout_id>/`                 | `workout_view`      | `workout`                 | Workout view for a specific workout |
| `workouts/`                                 | `workouts_view`     | `workouts`                | Workouts view                        |

---

## Model Creation Routes

These routes are used for creating new records in the database.

| **URL Pattern**                    | **View**                | **Name**                      | **Description**                  |
|-----------------------------------|-------------------------|-------------------------------|----------------------------------|
| `create_exercise/`                | `create_exercise`       | `create_exercise`            | Create a new exercise            |
| `create_exercise_record/`        | `create_exercise_record`| `create_exercise_record`     | Create a new exercise record    |
| `create_workout/`                 | `create_workout`        | `create_workout`             | Create a new workout            |
| `create_workout_record/`         | `create_workout_record` | `create_workout_record`      | Create a new workout record     |

---

## Model Deletion Routes

These routes are used for deleting records from the database.

| **URL Pattern**                                 | **View**                | **Name**                       | **Description**                   |
|------------------------------------------------|-------------------------|---------------------------------|-----------------------------------|
| `delete_exercise/<int:exercise_id>/`          | `delete_exercise`       | `delete_exercise`              | Delete an exercise by ID         |
| `delete_workout/<int:workout_id>/`            | `delete_workout`        | `delete_workout`               | Delete a workout by ID           |
| `delete_workout_record/<int:workout_record_id>/` | `delete_workout_record` | `delete_workout_record`       | Delete a workout record by ID    |

---

## Model Update Routes

These routes are used for updating existing records in the database.

| **URL Pattern**                           | **View**                 | **Name**                     | **Description**                   |
|--------------------------------------------|--------------------------|-----------------------------|-----------------------------------|
| `update_exercise/<int:exercise_id>/`      | `update_exercise`        | `update_exercise`          | Update an exercise by ID         |
| `update_workout/<int:workout_id>/`        | `update_workout`         | `update_workout`           | Update a workout by ID           |
| `update_workout_record/<int:workout_record_id>/` | `update_workout_record`  | `update_workout_record`   | Update a workout record by ID    |

---
=======

