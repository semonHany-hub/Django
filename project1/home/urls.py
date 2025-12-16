from django.urls import path
from .views import (welcome_view, training_tracks)

urlpatterns=[
    path('', welcome_view, name="welcome message"),
    path("training-tracks/", training_tracks),
]