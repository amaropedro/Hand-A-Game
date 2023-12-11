from django import forms
from .models import Genre, Platform

class AddGameForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=100)
    img = forms.ImageField(label="Capa")
    rental = forms.IntegerField(label="Tempo Maximo de Aluguel", min_value=1)
    price = forms.DecimalField(label="Preço", min_value=0)
    p = Platform.objects.values_list('id', 'platformName')
    platform = forms.ChoiceField(label="Plataforma", choices=p)
    g = Genre.objects.values_list('id', 'genreName')
    genres = forms.MultipleChoiceField(label="Generos", choices=g)
    isAvailable = forms.BooleanField(label="Disponivel para alugar?", required=False)
    isPhysical = forms.BooleanField(label="É fisico?", required=False)
    
class EditUserForm(forms.Form):
    name = forms.CharField(label="Nome de usuário", max_length=200)
    email = forms.EmailField(label="Email")
    city = forms.CharField(label="Cidade", max_length=200)
    phone = forms.CharField(label="Telefone", max_length=200)

class SearchForm(forms.Form):
    OPÇÕES_SELECT = [
        ('qualquer', 'qualquer'),
        ('30', '30 dias'),
        ('60', '60 dias'),
        ('90', '90 dias'),
        ('120', '120 dias'),
        ('150', '150 dias'),
    ]

    days = forms.ChoiceField(
        choices=OPÇÕES_SELECT, 
        label='Quantidade de dias'
    )