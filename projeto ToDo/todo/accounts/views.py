from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy # ele é parecido com o redirect, visto anteriormente, só que é o que é permitido para usar em views

from django.views import generic # que é o que deixa criar classes dentro da view

class SignUp(generic.CreateView): # chama o generic para criar uma view
    form_class = UserCreationForm # a classe do formulario
    # sucess_url = reverse_lazy('login') # url de sucesso, para que quando o user consiga se registrar ele logue no site
    template_name = 'registration/register.html' # register.html que está na pasta templates raiz
    
    def get_success_url(self): # deve-se adicionar o reverse_lazy assim, para o django redirecionar o user para a area de login ao se registrar
        return reverse_lazy('login')