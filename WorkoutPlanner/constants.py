# Page routes
INDEX_URL = ''
CALENDAR_URL = 'calendar/'
CALENDAR_WITH_PARAMS_URL = 'calendar/<int:year>/<int:month>/'
EXERCISES_URL = 'exercises/'
GYMBUDDY_URL = 'gymbuddy/<int:workout_id>'
WORKOUT_URL = 'workout/<int:workout_id>/'
WORKOUTS_URL = 'workouts/'

# Model creation routes
CREATE_EXERCISE_URL = 'create_exercise/'
CREATE_EXERCISE_RECORD_URL = 'create_exercise_record/'
CREATE_WORKOUT_URL = 'create_workout/'
CREATE_WORKOUT_RECORD_URL = 'create_workout_record/'

# Model deletion routes
DELETE_EXERCISE_URL = 'delete_exercise/<int:exercise_id>/'
DELETE_WORKOUT_URL = 'delete_workout/<int:workout_id>/'
DELETE_WORKOUT_RECORD_URL = 'delete_workout_record/<int:workout_record_id>/'

# Model update routes
UPDATE_EXERCISE_URL = 'update_exercise/<int:exercise_id>/'
UPDATE_WORKOUT_URL = 'update_workout/<int:workout_id>/'
UPDATE_WORKOUT_RECORD_URL = 'update_workout_record/<int:workout_record_id>/'

# View names
INDEX_NAME = 'index'
CALENDAR_NAME = 'calendar'
CALENDAR_WITH_PARAMS_NAME = 'calendar_with_params'
EXERCISES_NAME = 'exercises'
GYMBUDDY_NAME = 'gymbuddy'
WORKOUT_NAME = 'workout'
WORKOUTS_NAME = 'workouts'

# Model names
CREATE_EXERCISE_NAME = 'create_exercise'
CREATE_EXERCISE_RECORD_NAME = 'create_exercise_record'
CREATE_WORKOUT_NAME = 'create_workout'
CREATE_WORKOUT_RECORD_NAME = 'create_workout_record'
DELETE_EXERCISE_NAME = 'delete_exercise'
DELETE_WORKOUT_NAME = 'delete_workout'
DELETE_WORKOUT_RECORD_NAME = 'delete_workout_record'
UPDATE_EXERCISE_NAME = 'update_exercise'
UPDATE_WORKOUT_NAME = 'update_workout'
UPDATE_WORKOUT_RECORD_NAME = 'update_workout_record'
