from django.db import models


class Profile(models.Model):
    notification_token = models.CharField(max_length=100)
    id_token = models.CharField(max_length=100)
