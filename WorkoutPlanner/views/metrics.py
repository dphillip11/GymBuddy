from WorkoutPlanner.models import ExerciseRecord, Exercise
from django.db.models import Q, Sum, F, Max

def fetch_exercise_records(exercise_id=None, muscle_group_id=None, metric="volume", start_date=None, end_date=None):
    # Initialize the query set
    records = ExerciseRecord.objects.all()

    # Apply filters
    if exercise_id:
        records = records.filter(exercise_id=exercise_id)

    if start_date and end_date:
        records = records.filter(date__range=[start_date, end_date])
    elif start_date:
        records = records.filter(date__gte=start_date)
    elif end_date:
        records = records.filter(date__lte=end_date)

    if muscle_group_id:
        records = records.filter(exercise__muscle_groups__id=muscle_group_id)

    data = []

    if metric == "volume":
        records = records.annotate(volume=F('weight') * F('reps')).values('date').annotate(total_volume=Sum('volume')).order_by('date')

        # Prepare data for JSON response
        for record in records:
            data.append({
                'date': record['date'].strftime('%Y-%m-%d'),
                'volume': record['total_volume'],
            })

        return {
            'data': data, 
            'metric': metric
        }
    
    elif metric == "max_lift":
        records = records.values('date').annotate(max_lift=Max('weight')).order_by('date')

        # Prepare data for JSON response
        for record in records:
            data.append({
                'date': record['date'].strftime('%Y-%m-%d'),
                'max_lift': record['max_lift'],
            })
            
        return {
            'data': data, 
            'metric': metric
        }