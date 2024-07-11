document.addEventListener('DOMContentLoaded', () => {
    const csrfToken = window.csrfToken;

    /**
     * Generate URL for the get_active_workout_item endpoint
     * @param {number} exerciseId - The exercise ID to be included in the URL
     * @returns {string} - The complete URL with the exercise ID
     */
    function getActiveWorkoutItemUrl(exerciseId) {
        return window.urls.getActiveWorkoutItem.replace('exercise_id=0', `exercise_id=${exerciseId}`);
    }

    /**
     * Generate URL for the get_calendar_item endpoint
     * @param {number} year - The year to be included in the URL
     * @param {number} month - The month to be included in the URL
     * @param {number} day - The day to be included in the URL
     * @returns {string} - The complete URL with the year, month, and day
     */
    function getCalendarItemUrl(year, month, day) {
        return window.urls.getCalendarItem
            .replace('year=0', `year=${year}`)
            .replace('month=0', `month=${month}`)
            .replace('day=0', `day=${day}`);
    }

    /**
     * Generate URL for the get_workout_detail_item endpoint
     * @param {number} workoutId - The workout ID to be included in the URL
     * @returns {string} - The complete URL with the workout ID
     */
    function getWorkoutDetailItemUrl(workoutId) {
        return window.urls.getWorkoutDetailItem.replace('workout_id=0', `workout_id=${workoutId}`);
    }

    /**
     * Generate URL for the get_exercise_detail_item endpoint
     * @param {number} exerciseId - The exercise ID to be included in the URL
     * @returns {string} - The complete URL with the exercise ID
     */
    function getExerciseDetailItemUrl(exerciseId) {
        return window.urls.getExerciseDetailItem.replace('exercise_id=0', `exercise_id=${exerciseId}`);
    }

    /**
     * Generate URL for the get_exercise_records_item endpoint
     * @param {number} exerciseId - The exercise ID to be included in the URL
     * @param {number} year - The year to be included in the URL
     * @param {number} month - The month to be included in the URL
     * @param {number} day - The day to be included in the URL
     * @returns {string} - The complete URL with the exercise ID, year, month, and day
     */
    function getExerciseRecordsItemUrl(exerciseId, year, month, day) {
        return window.urls.getExerciseRecordsItem
            .replace('exercise_id=0', `exercise_id=${exerciseId}`)
            .replace('year=0', `year=${year}`)
            .replace('month=0', `month=${month}`)
            .replace('day=0', `day=${day}`);
    }

    /**
     * Helper method to fetch data from a URL
     * @param {string} url - The URL to fetch data from
     * @param {Object} options - Fetch options including method, headers, and body
     * @returns {Promise} - A promise resolving to the response data
     */
    function fetchData(url, options) {
        return fetch(url, options)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => data)
            .catch(error => {
                console.error('Fetch error:', error);
                throw error;
            });
    }

    /**
     * Example function to fetch active workout item data
     * @param {number} exerciseId - The exercise ID to be included in the URL
     * @returns {Promise} - A promise resolving to the fetched data
     */
    function fetchActiveWorkoutItem(exerciseId) {
        const url = getActiveWorkoutItemUrl(exerciseId);
        return fetchData(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            }
        });
    }

    /**
     * Example function to fetch calendar item data
     * @param {number} year - The year to be included in the URL
     * @param {number} month - The month to be included in the URL
     * @param {number} day - The day to be included in the URL
     * @returns {Promise} - A promise resolving to the fetched data
     */
    function fetchCalendarItem(year, month, day) {
        const url = getCalendarItemUrl(year, month, day);
        return fetchData(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            }
        });
    }

    /**
     * Example function to fetch workout detail item data
     * @param {number} workoutId - The workout ID to be included in the URL
     * @returns {Promise} - A promise resolving to the fetched data
     */
    function fetchWorkoutDetailItem(workoutId) {
        const url = getWorkoutDetailItemUrl(workoutId);
        return fetchData(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            }
        });
    }

    /**
     * Example function to fetch exercise detail item data
     * @param {number} exerciseId - The exercise ID to be included in the URL
     * @returns {Promise} - A promise resolving to the fetched data
     */
    function fetchExerciseDetailItem(exerciseId) {
        const url = getExerciseDetailItemUrl(exerciseId);
        return fetchData(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            }
        });
    }

    /**
     * Example function to fetch exercise records item data
     * @param {number} exerciseId - The exercise ID to be included in the URL
     * @param {number} year - The year to be included in the URL
     * @param {number} month - The month to be included in the URL
     * @param {number} day - The day to be included in the URL
     * @returns {Promise} - A promise resolving to the fetched data
     */
    function fetchExerciseRecordsItem(exerciseId, year, month, day) {
        const url = getExerciseRecordsItemUrl(exerciseId, year, month, day);
        return fetchData(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            }
        });
    }
});