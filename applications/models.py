from django.db import models

class Application(models.Model):
  company = models.CharField(max_length=200)
  link = models.URLField(max_length=256)
  role = models.CharField(max_length=200)
  type_of_position = models.CharField(max_length=50)
  description = models.TextField()
  type_of_application = models.CharField(max_length=75)
  response = models.CharField(max_length=100)
