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
  logo = models.ImageField()
  
  def __str__(self):
    return self.platformName

class Game(models.Model):
  title = models.CharField(max_length=200)
  isRented = models.BooleanField()
  isPhysical = models.BooleanField()
  cover =  models.ImageField()
  rentalDuration = models.IntegerField()
  price = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
  isAvailableToRent = models.BooleanField()

  platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  genres = models.ManyToManyField('Genre')
  
  def __str__(self):
    return self.title

class Genre(models.Model):
  genreName = models.CharField(max_length=200)
  
  def __str__(self):
    return self.genreName

class RentalManager(models.Model):
  initialDate = models.DateField()

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  game = models.ForeignKey(Game, on_delete=models.CASCADE)

  def __str__(self):
    return f"Jogo {self.game} alugado por {self.user} em {self.initialDate}"
  
class Notification(models.Model):
  content = models.CharField(max_length=4999)
  date = models.DateField()

  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.content}"