from django.db import models
from django.contrib.auth.models import User



class Game (models.Model):
    result =models.IntegerField(null=True)
    cost = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Game {self.cost} mrtyui"

class Item (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    buy_time = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Balance (models.Model):
    count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.user.name}"
