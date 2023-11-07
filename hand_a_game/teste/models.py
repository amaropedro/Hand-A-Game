from django.db import models
from django.utils import timezone

# Create your models here.
import datetime

class User(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  city = models.CharField(max_length=200)
  contact = models.CharField(max_length=200)
  password = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Platform(models.Model):
  platformName = models.CharField(max_length=200)
  allowsSimultaneousRentals = models.BooleanField()
  
  def __str__(self):
    return self.platformName

class Game(models.Model):
  title = models.CharField(max_length=200)
  isRented = models.BooleanField()
  isPhysical = models.BooleanField()
  cover =  models.ImageField()
  rentalDuration = models.IntegerField()
  platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title

class Genres(models.Model):
  game = models.ForeignKey(Game, on_delete=models.CASCADE)
  genreName = models.CharField(max_length=200)
  
  def __str__(self):
    return self.genreName
  