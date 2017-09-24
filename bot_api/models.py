from django.db import models


class CueUser(models.Model):

    user_id = models.CharField(max_length=100)
    iso_timezone = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Event(models.Model):

    user = models.CharField(max_length=100)

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    iso_timezone = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()

