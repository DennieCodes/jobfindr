from django.shortcuts import render, get_object_or_404, redirect
from applications.models import Application
from applications.forms import ApplicationForm, ApplicationFullForm
from django.contrib.auth.decorators import login_required

# DELETE_APPLICATION
@login_required
def delete_application(request, id):
  application = get_object_or_404(Application, id=id)
  application.delete()
  return redirect("list_applications")

# UPDATE_APPLICATION
@login_required
def update_application(request, id):
  application = get_object_or_404(Application, id=id)
  applications = Application.objects.filter(applicant=request.user)

  if request.method == "POST":
    form = ApplicationFullForm(request.POST, instance=application)
    if form.is_valid():
      form.save()
      return redirect("list_applications")
  else:
    form = ApplicationFullForm(instance=application)

  context = {
    "applications": applications,
    "application": application,
    "form": form
  }

  return render(request, "applications/update.html", context)

# LIST_APPLICATIONS
@login_required
def list_applications(request):
  applications = Application.objects.filter(applicant=request.user)

  if request.method == "POST":
    form = ApplicationForm(request.POST)
    if form.is_valid():
      application = form.save(False)
      application.applicant = request.user
      application.save()
      # return redirect

  form = ApplicationForm()

  context = {
    "applications": applications,
    "form": form,
  }

  return render(request, "applications/list_applications.html", context)