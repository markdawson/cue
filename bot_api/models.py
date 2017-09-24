from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=100)

class Event(models.Model):

    user_id = models.CharField(max_length=100)

    location = models.CharField(max_length=200)
    datetime = models.DateTimeField()

