from django.shortcuts import render
from .models import GameBoard


# Create your views here.

def homePage(request):

    list_games = GameBoard.objects.all()

    return render(request, 'gameboard/home.html',
                  context={"app_name": "Gameboard", "list_games": list_games})

def gamePage(request, game_id):

    game = GameBoard.objects.get(id=game_id)
    game.description_trunc = game.description.split('.')[0].strip()+'.'


    return render(request, 'gameboard/game.html',
                  context={"game": game})

def loginPage(request):
    return render(request, 'gameboard/login.html')

def registerPage(request):
    return render(request, 'gameboard/register.html')

def profilPage(request):
    return render(request, 'gameboard/profil.html')