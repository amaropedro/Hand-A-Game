from django.shortcuts import render

from .models import Game

# Create your views here.
def listTest(request):
    allGames = Game.objects.order_by('user')
    context = {'games_list': allGames}
    return render(request, 'main/index.html', context)