from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.messages import constants
from django.contrib import messages


# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.add_message(request, messages.ERROR, 'Senha e confirmar senha devem ser iguais!')
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, messages.ERROR, 'A senha deve conter 6 ou mais caracteres!')
            return redirect('/usuarios/cadastro')
        
        user = User.objects.filter(username=username)
        if user.exists():
            messages.add_message(request, messages.ERROR, 'Ja existe um usuario com este Username!')
            return redirect('/usuarios/cadastro')

        User.objects.create_user(
            username = username,
            password = senha,
        )
        return redirect('/usuarios/login')