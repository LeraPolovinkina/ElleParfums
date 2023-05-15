from datetime import datetime
from colorfield.fields import ColorField
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
    use_start_of_month = models.BooleanField(default=True)
    success_color = ColorField(default="#529653")
    show_users_15_and_20_percent = models.BooleanField(default=True)
    pizza_sound = models.FileField(upload_to='static/sounds/', default='static/sounds/pizza.mp3')
    sale_sound = models.FileField(upload_to='static/sounds/', default='static/sounds/sale.mp3')
    date_turn_on = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Static Values'
