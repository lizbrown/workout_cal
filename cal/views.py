from collections import defaultdict
from datetime import datetime, timedelta
from django.shortcuts import render
from cal.models import WorkoutSession


def workoutsession_list(request):
    # Get workouts for the last n weekdks
    # 
    today = datetime.today()
    #today = datetime(2016, 12, 11, 0, 0 , 0)
    day = today.weekday()
    #raise Exception(day)
    if day == 6:
        day = 0
    else:
        day += 1
    end_date = today + timedelta(6 - day)
    #raise Exception(end_date)
    start_date = end_date - timedelta(weeks=4, days=-1)
    #raise Exception(start_date)
    workouts = (WorkoutSession.objects.filter(user__username="liz",
                                              completed_date__gte=start_date)
                                      .order_by('completed_date'))
                                      #.values('completed_date', 'workout'))

    # Initialize dict with entry for every day
    by_day = dict() #defaultdict(list)
    for i in range((end_date - start_date).days + 1):
        date = (start_date + timedelta(days=i)).date()
        by_day[date] = []
    #raise Exception(by_day)

    # Put workouts on their day
    for workout in workouts:
        by_day[workout.completed_date].append(workout.workout.name)

    by_week = []
    for w in range(0, 4):
        week = []
        for d in range(0, 7):
            target_date = (start_date + timedelta(weeks=w, days=d)).date()
            week.append({target_date.day: by_day[target_date]})
        by_week.append(week)

    #raise Exception(by_week)
 
    return render(request,
                  'cal/workoutsession_list.html',
                  {'by_week': by_week})
