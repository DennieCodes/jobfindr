from django.db import models
from django.conf import settings
from datetime import date
from applications.types import ApplicationStatus, Screening, Assessment, Offer

class Application(models.Model):
  name=models.CharField(max_length=200)
  company = models.CharField(max_length=200)
  link = models.URLField(max_length=256)
  role = models.CharField(max_length=200)
  description = models.TextField()
  date_applied = models.DateField(default=date.today)
  application_status = models.CharField(
    max_length=1,
    choices=ApplicationStatus.choices,
    default=ApplicationStatus.NORESPONSE
  )

  screening = models.CharField(
    max_length = 1,
    choices=Screening.choices,
    default=Screening.AWAITING
  )

  assessment = models.CharField(
    max_length=1,
    choices=Assessment.choices,
    default=Assessment.AWAITING
  )

  interview = models.CharField(
    max_length=1,
    choices=Assessment.choices,
    default=Assessment.AWAITING
  )

  offer = models.CharField(
    max_length=1,
    choices=Offer.choices,
    default=Offer.AWAITING
  )

  applicant=models.ForeignKey(
    settings.AUTH_USER_MODEL,
    related_name="applications",
    on_delete=models.CASCADE,
  )

  def __str__(self):
    return self.name

  class Meta:
    ordering = ["company"]