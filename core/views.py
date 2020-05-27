from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required #requer autenticação nesta pagina
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def umidade(request, city, days):
    return HttpResponse('<h1>City: {city} Days: {days}!!!</h1>'.format(city=city, days=days))

@login_required(login_url='/login/')
def calculadora(request, operacao, a, b):
    calculadoraOP = {
        'soma': lambda a, b: a + b,
        'subtração': lambda a, b: a - b,
        'divisão': lambda a, b: a / b,
        'multiplicação': lambda a, b: a * b,
    }
    resultado = calculadoraOP[operacao](a, b)
    return HttpResponse('<h1>A {operacao} de: {a} e {b} é igual a {resultado}!!!</h1>'.format(a=a, b=b, resultado=resultado, operacao=operacao))

@login_required(login_url='/login/')
def lista_cidades(request):
    usuario = request.user #usario da seção
    evento = Evento.objects.filter(usuario=usuario) #filtar pelo usuário logado
    dados = {'eventos':evento}
    return render(request, 'cidades.html', dados)

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "USUÁRIO OU SENHA INVALIDO!!!")

    return redirect('/')
