from datetime import datetime

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    profit = models.IntegerField(default=0)
    user_id = models.IntegerField()
    is_active = models.BooleanField(default=True)
    goal = models.IntegerField(default=500000)


class StaticValue(models.Model):
    global_goal = models.IntegerField(default=500000)
    employee_goal = models.IntegerField(default=100000)
    today_goal = models.IntegerField(default=100000)
    token = models.CharField(max_length=200, default="")
    date = models.DateField(default=datetime.now())
    class Meta:
        verbose_name_plural = 'Static Values'
