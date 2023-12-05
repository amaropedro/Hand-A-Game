from django.shortcuts import render

from .models import Game, User, Platform, Genre

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

import os
from django.conf import settings

# Create your views here.
def signup_view(request):
    
    if request.method == 'POST':
        # Recupera os dados do formulário do request
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        city = request.POST['city']
        phone = request.POST['phone']

        User.objects.create_user(
            email=email, 
            username=username, 
            password=password, 
            city=city, 
            phone=phone
        )
        
        # Autentica o usuário
        user = authenticate(request, email=email, password=password)    
        if user is not None:
            print("OK, deu certo!")
            login(request, user)
            return redirect('home')
        
    return render(request, 'main/signup.html')
        
def login_view(request):
    if request.method == 'POST':
        # Recupera os dados do formulário do request
        email = request.POST['email']
        password = request.POST['password']

        # Autentica o usuário
        user = authenticate(request, email=email, password=password)

        if user is not None:
            print("OK, deu certo!")
            # Se o usuário foi autenticado com sucesso, faça o login
            login(request, user)
            # Redirecione para a página de sucesso ou qualquer outra página desejada
            # 'home': é o nome da view
            return redirect('home')
        else:
            print("OPS, não foi!")
            print(email, password)
            # Se a autenticação falhar, você pode tratar isso de acordo
            return render(request, 'main/login.html', {
                'erro': 'Credenciais inválidas'
            })

    # Se o método da requisição não for POST, apenas renderize o formulário de login
    return render(request, 'main/login.html')

def home_view(request):
    if request.user.is_authenticated:
        games = Game.objects.exclude(user=request.user)
        platforms = Platform.objects.all()

        return render(request, 'main/home.html', {
            'games_list': games,
            'platforms': platforms,
        })
    return redirect('login')

def myGames_view(request):
    if request.user.is_authenticated:
        userGames = Game.objects.filter(user=request.user)
        return render(request, 'main/myGames.html', {
            'games_list': userGames
        })
    return redirect('login')

def addGame_view(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            name = request.POST['name']
            # img = request.FILES['img']
            
            # with open(os.path.join(settings.MEDIA_ROOT, 'images/games', img.name), 'wb') as destination:
            #     for chunk in img.chunks():
            #         destination.write(chunk)
            
            # isPhysical = request.POST['isPhysical']
            # isAvailable = request.POST['isAvailable']
            rental = request.POST['rentalDuration']
            price = request.POST['price']
            #platform = request.POST['platform']
            #genres = request.POST['genres']
            user = request.user
            
            Game().add_game(title=name,
                          isPhysical=False, #mudar
                          cover=None, #mudar
                          rentalDuration=rental,
                          price=price,
                          isAvailable=True, #mudar
                          platform=Platform.objects.filter(platformName='PS4')[0], #mudar
                          genres=Genre.objects.all(), #mudar
                          user=user
                          )
            
            return redirect('myGames')
        
        platforms = Platform.objects.all()
        genres = Genre.objects.all()
        return render(request, 'main/addGame.html', {
            'platforms': platforms,
            'genres': genres
        })
    return redirect('login')