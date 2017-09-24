from django.db import models


class CueUser(models.Model):

    user_id = models.CharField(max_length=100)
    iso_timezone = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    home_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    home_long = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):

    user = models.CharField(max_length=100)

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    iso_timezone = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.user + ': ' + self.title

