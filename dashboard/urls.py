from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.home_view, name='home'),
    url(r"^user/(?P<name>)", views.user_view, name="user")
]