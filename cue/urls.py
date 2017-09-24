from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("dashboard.urls", namespace="dashboard")),
    url(r'^api/', include("bot_api.urls", namespace="bot_api"))
]