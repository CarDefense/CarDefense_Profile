from django.db import models
# from django.contrib.postgres.fields import ArrayField, JSONField


class Profile(models.Model):
    id_user = models.IntegerField()
    notification_token = models.CharField(max_length=50)
    # notification = ArrayField(JSONField(True))
