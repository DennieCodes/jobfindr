from django.contrib import admin
from applications.models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
  list_display = (
    "company",
    "link",
    "role",
    "description",
  )