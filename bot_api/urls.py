from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^messages$", views.messages_response, name='messages'),
    url(r"^messages/verify$", views.messages_response_verify, name='messages'),
]