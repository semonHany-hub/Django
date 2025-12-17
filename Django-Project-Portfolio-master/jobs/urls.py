from django.urls import path
from .views import show_details

urlpatterns=[
    path('<int:job_id>/', show_details, name="details"),
]