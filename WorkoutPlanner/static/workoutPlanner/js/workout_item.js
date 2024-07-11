document.addEventListener('DOMContentLoaded', () => {
    const csrfToken = window.csrfToken;

    document.querySelectorAll('.exercise-form').forEach(form => {
        new AjaxRequestBuilder(`#${form.id}`)
            .onEvent('submit')
            .withPost('add_exercise_record/') // Adjust the URL to match your endpoint
            .withParams({
                exercise_id: form.querySelector('input[name="exercise_id"]').value,
                reps: form.querySelector('input[name="reps"]').value,
                weight: form.querySelector('input[name="weight"]').value,
            })
            .onSuccess(() => {
                const exerciseId = form.querySelector('input[name="exercise_id"]').value;
                document.querySelector(`#wi_${exerciseId}`).innerHTML = fetch;
            })
            .onError(error => {
                console.error('Error:', error);
            })
            .build();
    });
});