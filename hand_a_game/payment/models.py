from django.db import models
from main.models import RentalManager
import datetime

# Create your models here.
class PaymentManager(models.Model):
  date = models.DateField()
  isPayed = models.BooleanField(default=False)
  
  def handle_payment(self, user, game):
    self.isPayed = True
    self.date = datetime.datetime.now()
    self.save()
    
    RentalManager.borrowGame(user, game)