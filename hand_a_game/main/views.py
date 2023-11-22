from django.shortcuts import render

from .models import Game, User

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def listTest(request):
    allGames = Game.objects.order_by('user')
    context = {'games_list': allGames}
    return render(request, 'main/index.html', context)

def login_view(request):
    if request.method == 'POST':
        # Recupera os dados do formulário do request
        email = request.POST['email']
        password = request.POST['password']

        # Autentica o usuário
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # # Se o usuário foi autenticado com sucesso, faça o login
            # login(request, user)
            # # Redirecione para a página de sucesso ou qualquer outra página desejada
            # return redirect('pagina_de_sucesso')
            print("OK, deu certo!")
        else:
            print("OPS")

            # Se a autenticação falhar, você pode tratar isso de acordo
            return render(request, 'main/login.html', {
                'erro': 'Credenciais inválidas'
            })

    # Se o método da requisição não for POST, apenas renderize o formulário de login
    return render(request, 'main/login.html')