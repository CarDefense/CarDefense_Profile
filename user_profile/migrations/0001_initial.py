# Generated by Django 2.1 on 2018-10-31 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_token', models.CharField(max_length=100)),
                ('id_token', models.IntegerField()),
            ],
        ),
    ]
