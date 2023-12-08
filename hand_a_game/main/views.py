from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import Game, User, Platform, Genre
from .forms import AddGameForm, EditUserForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

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
    if request.user.is_authenticated:
        return redirect('home')
    
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

def logout_view(request):
    logout(request)
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

        erro = request.session.pop('error_in_delete', '')

        userGames = Game.objects.filter(user=request.user)
        return render(request, 'main/myGames.html', {
            'games_list': userGames,
            'erro': erro
        })
    
    return redirect('login')

def addGame_view(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            form = AddGameForm(request.POST, request.FILES)
            if form.is_valid():            
                img = form.cleaned_data['img']

                platform = Platform.objects.filter(id=form.cleaned_data['platform'])[0]
                                
                Game().add_game(
                    title=form.cleaned_data['name'],
                    isPhysical=form.cleaned_data['isPhysical'],
                    cover=img,
                    rentalDuration=form.cleaned_data['rental'],
                    price=form.cleaned_data['price'],
                    isAvailable=form.cleaned_data['isAvailable'],
                    platform=platform,
                    genres=form.cleaned_data['genres'],
                    user=request.user
                )
                
                return redirect('myGames')
        else:
            form = AddGameForm()
        
        platforms = Platform.objects.all()
        genres = Genre.objects.all()
        return render(request, 'main/addGame.html', {
            'platforms': platforms,
            'genres': genres,
            'form' : form
        })
    return redirect('login')

def editGame_view(request, id):
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = AddGameForm(request.POST, request.FILES)

            if form.is_valid():            
                img = form.cleaned_data['img']

                platform = Platform.objects.filter(id=form.cleaned_data['platform'])[0]
                
                game = Game.objects.filter(id=id)[0]
                game.edit_game(
                    title=form.cleaned_data['name'],
                    isPhysical=form.cleaned_data['isPhysical'],
                    cover=img,
                    rentalDuration=form.cleaned_data['rental'],
                    price=form.cleaned_data['price'],
                    isAvailable=form.cleaned_data['isAvailable'],
                    platform=platform,
                    genres=form.cleaned_data['genres'],
                )

                return redirect('myGames')

            else:
                print("Formulário não é válido!")

        try:
            game = get_object_or_404(Game, id=id)
            if game.user == request.user:
            
                form = AddGameForm(initial={
                    'name': game.title,
                    'rental': game.rentalDuration,
                    'price': game.price,
                    'platform': game.platform,

                    'isAvailable': game.isAvailableToRent,
                    'isPhysical': game.isPhysical,
                })

                return render(request, 'main/editGame.html', {
                    'game': game,
                    'form': form
                })
            else:
                return redirect('myGames')

        except Http404:
            request.session['error_in_delete'] = 'O jogo não foi encontrado!'
            return redirect('myGames')

    return redirect('login')

def delete_view(request, id):
    if request.user.is_authenticated:

        try:
            # Recupera o objeto (registro) do banco de dados
            game = get_object_or_404(Game, id=id)

            if game.user == request.user:
                # Exclui o objeto do banco de dados
                game.delete()

        except Http404:
            request.session['error_in_delete'] = 'O jogo não foi encontrado!'
            return redirect('myGames')

        return redirect('myGames')
    return redirect('login')

def editUser_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pass

        form = EditUserForm(initial={
            'name': request.user.username,
            'email': request.user.email,
            'city': request.user.city,
            'phone': request.user.phone,
        })
        return render(request, 'main/editUser.html', {
            'form': form
        })
    return redirect('login')