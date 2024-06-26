from datetime import datetime
from colorfield.fields import ColorField
from django.db import models

from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class UserVictory(models.Model):
    name = models.CharField(max_length=100)
    profit = models.IntegerField(default=0)
    user_id = models.IntegerField()
    is_active = models.BooleanField(default=True)
    goal = models.IntegerField(default=500000)

class UserEnglishDistrict(models.Model):
    name = models.CharField(max_length=100)
    profit = models.IntegerField(default=0)
    user_id = models.IntegerField()
    is_active = models.BooleanField(default=True)
    goal = models.IntegerField(default=500000)

class StaticValueVictory(models.Model):
    global_goal = models.IntegerField(default=500000)
    employee_goal = models.IntegerField(default=100000)
    today_goal = models.IntegerField(default=100000)
    token = models.CharField(max_length=200, default="")
    date = models.DateField(default=datetime.now)
    use_start_of_month = models.BooleanField(default=True)
    success_color = ColorField(default="#529653")
    show_users_15_and_20_percent = models.BooleanField(default=True)
    pizza_sound = models.FileField(upload_to='static/sounds/', default='static/sounds/pizza.mp3')
    sale_sound = models.FileField(upload_to='static/sounds/', default='static/sounds/sale.mp3')
    date_turn_on = models.BooleanField(default=True)
    show_employees = models.BooleanField(default=True)
    message = models.TextField(max_length=300, default="", blank=True, null=True)

class StaticValueEnglishDistrict(models.Model):
    global_goal = models.IntegerField(default=500000)
    employee_goal = models.IntegerField(default=100000)
    today_goal = models.IntegerField(default=100000)
    token = models.CharField(max_length=200, default="")
    date = models.DateField(default=datetime.now)
    use_start_of_month = models.BooleanField(default=True)
    success_color = ColorField(default="#529653")
    show_users_15_and_20_percent = models.BooleanField(default=True)
    pizza_sound = models.FileField(upload_to='static/sounds/', default='static/sounds/pizza.mp3')
    sale_sound = models.FileField(upload_to='static/sounds/', default='static/sounds/sale.mp3')
    date_turn_on = models.BooleanField(default=True)
    show_employees = models.BooleanField(default=True)
    message = models.TextField(max_length=300, default="", blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Static Values English District'

@receiver(pre_save, sender=StaticValueVictory)
def delete_old_files(sender, instance, *args, **kwargs):
    if instance.pk:
        # Получаем предыдущий объект модели
        old_instance = sender.objects.get(pk=instance.pk)
        # Если новый файл для поля pizza_sound был загружен и он отличается от предыдущего, то удаляем старый файл
        if instance.pizza_sound and instance.pizza_sound != old_instance.pizza_sound:
            old_instance.pizza_sound.delete(save=False)
        # Если новый файл для поля sale_sound был загружен и он отличается от предыдущего, то удаляем старый файл
        if instance.sale_sound and instance.sale_sound != old_instance.sale_sound:
            old_instance.sale_sound.delete(save=False)

@receiver(pre_save, sender=StaticValueEnglishDistrict)
def delete_old_files(sender, instance, *args, **kwargs):
    if instance.pk:
        # Получаем предыдущий объект модели
        old_instance = sender.objects.get(pk=instance.pk)
        # Если новый файл для поля pizza_sound был загружен и он отличается от предыдущего, то удаляем старый файл
        if instance.pizza_sound and instance.pizza_sound != old_instance.pizza_sound:
            old_instance.pizza_sound.delete(save=False)
        # Если новый файл для поля sale_sound был загружен и он отличается от предыдущего, то удаляем старый файл
        if instance.sale_sound and instance.sale_sound != old_instance.sale_sound:
            old_instance.sale_sound.delete(save=False)