from django.forms import ModelForm
from applications.models import Application

class ApplicationForm(ModelForm):
  class Meta:
    model = Application
    fields = (
      "company",
      "link",
      "role",
      "description"
    )

class ApplicationFullForm(ModelForm):
  class Meta:
    model = Application
    fields = (
      "company",
      "link",
      "role",
      "description",
      "application_status",
      "screening",
      "assessment",
    )