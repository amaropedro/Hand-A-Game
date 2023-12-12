from django.db import models
from main.models import RentalManager, User, Game
import datetime

# Create your models here.
class PaymentManager(models.Model):
  date = models.DateField()
  isPayed = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
  game = models.ForeignKey(Game, on_delete=models.CASCADE, default=None)
  
  def handle_payment(self, user, game):
    self.isPayed = True
    self.date = datetime.datetime.now()
    self.user = user
    self.game = game
    self.save()
    
    RentalManager.borrowGame(user, game)
    
  def __str__(self):
    return f"{self.user} pagou por {self.game.title}"