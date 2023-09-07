from django.shortcuts import render
from applications.models import Application

def list_applications(request):
  applications = Application.objects.all()

  context = {
    "applications": applications
  }

  return render(request, "applications/list_applications.html", context)