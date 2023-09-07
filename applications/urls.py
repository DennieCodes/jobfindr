from django.urls import path
from applications.views import list_applications

urlpatterns = [
  path("", list_applications, name="list_applications")
]