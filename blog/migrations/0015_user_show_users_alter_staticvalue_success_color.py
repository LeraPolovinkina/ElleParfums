# Generated by Django 4.2.5 on 2023-09-21 15:28

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_staticvalue_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='show_users',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='staticvalue',
            name='success_color',
            field=colorfield.fields.ColorField(default='#529653', image_field=None, max_length=25, samples=None),
        ),
    ]
