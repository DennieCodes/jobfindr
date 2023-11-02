from django.db import models

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