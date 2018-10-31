from django.shortcuts import render
from gameplay.models import Game

def home(request):
    player_games=Game.object.game_for_user(request.user)
    active_games=player_games.active_games()
    return render(request, "player/home.html"
                  ,{'player_games':active_games})
