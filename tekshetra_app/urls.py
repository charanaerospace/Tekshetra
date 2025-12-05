from django.urls import path
from .views import submit_professional

urlpatterns = [
    path("submit/", submit_professional),
]
