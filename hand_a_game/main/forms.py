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
    
    def clean_img(self):
        print("Dentro do método!")
        # Se a imagem já foi fornecida no formulário inicial, ignorar a validação
        if 'img' in self.initial:
            return self.initial['img']

        # Caso contrário, continue com a validação padrão
        img = self.cleaned_data.get('img', None)
        if not img:
            raise forms.ValidationError("Este campo é obrigatório.")
        return img