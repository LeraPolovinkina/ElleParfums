# Generated by Django 4.2.5 on 2023-11-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_alter_user_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='url',
            field=models.CharField(blank=True, default='http://127.0.0.1:8000/', max_length=255, null=True),
        ),
    ]
