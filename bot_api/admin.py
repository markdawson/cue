from django.contrib import admin
from .models import CueUser, Event, Place

admin.site.register(CueUser)
admin.site.register(Event)
admin.site.register(Place)