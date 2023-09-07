from django.db import models

class Application(models.Model):
  company = models.CharField(max_length=200)
  link = models.URLField(max_length=256)
  role = models.CharField(max_length=200)
  description = models.TextField()

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["company"]