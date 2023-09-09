from django.shortcuts import render
from applications.models import Application
from django.contrib.auth.decorators import login_required

# LIST_APPLICATIONS
@login_required
def list_applications(request):
  applications = Application.objects.filter(applicant=request.user)

  context = {
    "applications": applications
  }

  return render(request, "applications/list_applications.html", context)