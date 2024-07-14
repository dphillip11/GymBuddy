document.addEventListener('DOMContentLoaded', () => {
    let timerDisplay = document.getElementById('timer-display');
    let startButton = document.getElementById('start-button');
    let stopButton = document.getElementById('stop-button');
    let resetButton = document.getElementById('reset-button');
    let logExerciseButtons = document.querySelectorAll(".log-exercise");

    let startTime;
    let updatedTime;
    let difference;
    let timerInterval;
    let running = false;

    function startTimer() {
        if (!running) {
            startTime = new Date().getTime();
            timerInterval = setInterval(updateTimer, 1000);
            running = true;
        }
    }

    function stopTimer() {
        if (running) {
            clearInterval(timerInterval);
            running = false;
        }
    }

    function resetTimer() {
        clearInterval(timerInterval);
        timerDisplay.textContent = '00:00:00';
        running = false;
    }

    function updateTimer() {
        updatedTime = new Date().getTime();
        difference = updatedTime - startTime;

        let hours = Math.floor(difference / (1000 * 60 * 60));
        let minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
        let seconds = Math.floor((difference % (1000 * 60)) / 1000);

        hours = (hours < 10) ? "0" + hours : hours;
        minutes = (minutes < 10) ? "0" + minutes : minutes;
        seconds = (seconds < 10) ? "0" + seconds : seconds;

        timerDisplay.textContent = hours + ':' + minutes + ':' + seconds;
    }

    startButton.addEventListener('click', startTimer);
    stopButton.addEventListener('click', stopTimer);
    resetButton.addEventListener('click', resetTimer);

    logExerciseButtons.forEach(element => {
        element.addEventListener('click', startTimer);
    });
});
