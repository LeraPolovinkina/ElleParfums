# Generated by Django 4.2 on 2023-05-18 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_staticvalue_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticvalue',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 18, 15, 12, 30, 449806)),
        ),
    ]