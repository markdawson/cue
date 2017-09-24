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


class Place(models.Model):

    name = models.CharField(max_length=200, null=True)
    google_id = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.user + ': ' + self.title


class Event(models.Model):

    user = models.ForeignKey(CueUser, related_name="usergit")

    title = models.CharField(max_length=200)
    location = models.ForeignKey(Place, related_name="place", null=True)

    confirmed = models.BooleanField(default=False)
    iso_timezone = models.CharField(max_length=200, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user + ': ' + self.title




