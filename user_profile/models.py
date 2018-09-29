from django.db import models
# from django.contrib.postgres.fields import ArrayField, JSONField


class CarProfile(models.Model):
    notification_token = models.CharField(max_length=100)
    plate = models.CharField(max_length=7)
    car_model = models.CharField(max_length=20)
    car_color = models.CharField(max_length=10)


class Profile(models.Model):
    notification_token = models.CharField(max_length=100)
