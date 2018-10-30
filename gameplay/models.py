from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    first_player=models.ForeignKey(User, related_name="games_first_player", on_delete=models.DO_NOTHING)
    second_player=models.ForeignKey(User, related_name="games_second_player", on_delete=models.DO_NOTHING)
    start_time=models.DateTimeField(auto_now_add=True)
    last_action=models.DateTimeField(auto_now=True)

class Move(models.Model):
    x=models.IntegerField()
    y=models.IntegerField()
    comment=models.CharField(blank=True, max_length=50)
    by_first_player=models.BooleanField()
    game=models.ForeignKey(Game, on_delete=models.CASCADE)
