from django.db import models
from django.conf import settings

class Application(models.Model):
  name=models.CharField(max_length=200)
  company = models.CharField(max_length=200)
  link = models.URLField(max_length=256)
  role = models.CharField(max_length=200)
  description = models.TextField()

  applicant=models.ForeignKey(
    settings.AUTH_USER_MODEL,
    related_name="applications",
    on_delete=models.CASCADE,
  )

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["company"]