# Generated by Django 2.1 on 2018-09-28 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='notification',
        ),
    ]
