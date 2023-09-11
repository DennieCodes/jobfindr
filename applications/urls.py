from django.urls import path
from applications.views import list_applications, update_application

urlpatterns = [
  path("", list_applications, name="list_applications"),
  path("<int:id>/update/", update_application, name="update_application"),
]