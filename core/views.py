from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from core.models import Evento
from django.contrib.auth.decorators import login_required  # requer autenticação nesta pagina
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from core.forms import UserModelForm

# Create your views here.

def cadastro(request):
    logout(request)
    title = 'Acesse a Área Restrita para mais informações'
    form = UserModelForm(request.POST or None)
    context = {'form': form.errors,
               'title': title}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            context['sucesso'] = 'USUÁRIO CADASTRADO COM SUCESSO'
            return render(request, 'cidades.html', context)

    return render(request, 'usuarios/cadastro.html', context)

def login_user(request):
    title = 'Acesse a Área Restrita para mais informações'
    dados = {'title': title}
    return render(request, 'login.html', dados)


def logout_user(request):
    logout(request)
    return redirect('/')


# @login_required(login_url='/login/')
# def umidade(request, city, days):
#    return HttpResponse('<h1>City: {city} Days: {days}!!!</h1>'.format(city=city, days=days))

# @login_required(login_url='/login/')
# def calculadora(request, operacao, a, b):
#    calculadoraOP = {
#        'soma': lambda a, b: a + b,
#        'subtração': lambda a, b: a - b,
#        'divisão': lambda a, b: a / b,
#       'multiplicação': lambda a, b: a * b,
#   }
#   resultado = calculadoraOP[operacao](a, b)
#   return HttpResponse('<h1>A {operacao} de: {a} e {b} é igual a {resultado}!!!</h1>'.format(a=a, b=b, resultado=resultado, operacao=operacao))

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/cidades')
        else:
            messages.error(request, "USUÁRIO OU SENHA INVALIDO!!!")

    return redirect('/login')


def submit_cadastro(request):
    if request.POST:
        nome = request.POST.get('nome')
        cidade = request.POST.get('cidade')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        Evento.objects.create(
            nome=nome,
            cidade=cidade,
            username=username,
            email=email,
            password=password
        )
    return redirect('/login/cadastro/')


def inicial(request):
    title = 'Acesse a Área Restrita para mais informações'
    dados = {'title': title}
    return render(request, 'inicial.html', dados)


@login_required(login_url='/login/')
def lista_cidades(request):
    usuario = request.user  # usario da seção
    evento = Evento.objects.filter(usuario=usuario)  # filtar pelo usuário logado
    dados = {'eventos': evento}
    return render(request, 'cidades.html', dados)


@login_required(login_url='/login/')
def alterar(request):
    return render(request, 'alterar.html')

'''
def cadastro(request):
    title = 'Cadastre-se'
    dados = {'title': title}
    return render(request, 'cadastro.html', dados)


class register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login.html')
    template_name = 'register.html'
'''