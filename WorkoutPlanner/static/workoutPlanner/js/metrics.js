document.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('exerciseChart').getContext('2d');
    let exerciseChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Volume',
                data: [],
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'day'
                    }
                },
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    function updateGraph(data) {
        const labels = data.data.map(record => record.date);
        // Update the chart based on the selected metric
        if (data.metric === "volume") 
        {
            const volumes = data.data.map(record => record.volume);
            exerciseChart.data.labels = labels;
            exerciseChart.data.datasets[0].data = volumes;
            exerciseChart.data.datasets[0].label = 'Total Volume';
    
        } 
        else if (data.metric === "max_lift") 
        {
            const lifts = data.data.map(record => record.max_lift);
            exerciseChart.data.labels = labels;
            exerciseChart.data.datasets[0].data = lifts;
            exerciseChart.data.datasets[0].label = 'Max Lift';
        } 
        else 
        {
            console.error('Unsupported metric type:', data.metric);
            return;
        }
    
        exerciseChart.update();
    }

    const connectWebSocket = () => {
        const socket = new WebSocket('ws://localhost:8000/metrics/');

        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            updateGraph(data);
        };

        const form = document.getElementById('filter-form');

        form.addEventListener('submit', (event) => {
            event.preventDefault();
            const formData = new FormData(form);
            const exerciseId = formData.get('exercise');
            const muscleGroupId = formData.get('muscle_group');
            const metric = formData.get('metric');
            const startDate = formData.get('start_date');
            const endDate = formData.get('end_date');

            socket.send(JSON.stringify({
                exercise_id: exerciseId,
                muscle_group_id: muscleGroupId,
                metric: metric,
                start_date: startDate,
                end_date: endDate,
            }));
        });
    };

    connectWebSocket();
});