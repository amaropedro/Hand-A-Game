from django.db import models
from django.utils import timezone

# Create your models here.
import datetime

class User(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  city = models.CharField()
  contact = models.CharField()
  password = models.CharField()

  def __str__(self):
    return self.name
