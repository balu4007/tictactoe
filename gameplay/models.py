from django.db import models
from django.contrib.auth.models import User


GAME_STATUS_CHOICES=(
    ('F', 'First Player to Move'),
    ('S', 'Second Player to Move'),
    ('W', 'First Player Win'),
    ('L', 'Second Player Win'),
    ('D', 'Draw'),

)

class Game(models.Model):
    first_player=models.ForeignKey(User, related_name="games_first_player", on_delete=models.DO_NOTHING)
    second_player=models.ForeignKey(User, related_name="games_second_player", on_delete=models.DO_NOTHING)
    start_time=models.DateTimeField(auto_now_add=True)
    last_action=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=1, default='F',
                            choices=GAME_STATUS_CHOICES)
    def __str__(self):
        return "{0} vs {1}".format(self.first_player,self.second_player)

class Move(models.Model):
    x=models.IntegerField()
    y=models.IntegerField()
    comment=models.CharField(blank=True, max_length=50)
    by_first_player=models.BooleanField()
    game=models.ForeignKey(Game, on_delete=models.CASCADE)
