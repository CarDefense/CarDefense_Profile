from django.db import models


class Profile(models.Model):
    notification_token = models.CharField(max_length=100)
    id_token = models.BigIntegerField()
    document = models.CharField(null=True, blank=True, max_length=250)


class Document(models.Model):
    document = models.ImageField(null=True, blank=True)
