from django.db import models
from django.conf import settings
from enum import Enum

class ApplicationStatus(models.TextChoices):
  NORESPONSE = "N", "No Response"
  ADVANCING = "A", "Advancing"
  REJECTED = "R", "Rejected"

class Screening(models.TextChoices):
  AWAITING = "W", "Awaiting"
  ADVANCING = "A", "Advancing"
  REJECTED = "R", "Rejected"

class Assessment(models.TextChoices):
  AWAITING = "W", "Awaiting"
  ONGOING = "O", "On-going"
  PASSED = "P", "Passed"
  REJECTED = "R", "Rejected"

class Offer(models.TextChoices):
  AWAITING = "W", "Awaiting"
  COUNTER = "C", "Counter-offered"
  REJECTED = "R", "Rejected"
  ACCEPTED = "A", "Accepted"

class Application(models.Model):
  name=models.CharField(max_length=200)
  company = models.CharField(max_length=200)
  link = models.URLField(max_length=256)
  role = models.CharField(max_length=200)
  description = models.TextField()
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