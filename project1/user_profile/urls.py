from django.urls import path
from .views import (greeting_message, birth_date)

urlpatterns=[
    path("", greeting_message),
    path("birth-date", birth_date, name="BirthDate"),
]