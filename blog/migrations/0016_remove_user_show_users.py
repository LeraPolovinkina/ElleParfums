# Generated by Django 4.2.5 on 2023-09-21 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_user_show_users_alter_staticvalue_success_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='show_users',
        ),
    ]