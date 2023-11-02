from django.db import models
from django.conf import settings
from datetime import date
from contacts_microservice.models import Contacts

class User(models.Model):
  last_name = models.CharField(max_length=100)
  first_name = models.CharField(max_length=100)
  email = models.EmailField(max_length=254)
  password = models.CharField(max_length=200)
  verified = models.BooleanField(default=False)
  pronouns = models.CharField(max_length=50)
  joined = models.DateField(default=date.today)

  contacts = models.ForeignKey(
    Contacts,
    related_name="contacts",
    on_delete = models.CASCADE,
  )
