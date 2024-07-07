from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_practitioner = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields specific to students here

class Practitioner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields specific to practitioners here
