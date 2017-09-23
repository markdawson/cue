from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("dashboard.urls", namespace="dashboard")),
    #url(r'^api', include("messenger.urls", namespace="messenger"))
]