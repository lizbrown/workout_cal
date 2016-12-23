from django.db import models
from django.utils import timezone

class Workout(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorkoutSession(models.Model):
    workout = models.ForeignKey('Workout')
    user = models.ForeignKey('auth.User')
    completed_date = models.DateField(default=timezone.now)

    def __str__(self):
        return "{} {} {}".format(self.user, self.workout, self.completed_date)
