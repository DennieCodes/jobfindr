from django.forms import ModelForm
from applications.models import Application

class ApplicationForm(ModelForm):
  class Meta:
    model = Application
    fields = (
      "company",
      "link",
      "role",
      "description",
      "date_applied",
    )

class ApplicationFullForm(ModelForm):
  class Meta:
    model = Application
    fields = (
      "company",
      "link",
      "role",
      "description",
      "date_applied",
      "application_status",
      "screening",
      "assessment",
      "interview",
      "offer",
    )