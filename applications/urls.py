from django.urls import path
from applications.views import list_applications, update_application, delete_application

urlpatterns = [
  path("", list_applications, name="list_applications"),
  path("<int:id>/update/", update_application, name="update_application"),
  path("<int:id>/delete/", delete_application, name="delete_application"),
]