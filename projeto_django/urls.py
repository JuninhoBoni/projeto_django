"""projeto_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/inicial/')),
    path('admin/', admin.site.urls),
    # path('umidade/<city>/<int:days>/', views.umidade),
    # path('calculadora/<operacao>/<int:a>/<int:b>/', views.calculadora),
    path('login/', views.login_user, name='login'),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('cidades/', views.lista_cidades, name='cidades'),
    path('inicial/', views.inicial),
    path('alterar/', views.alterar),
    path('usuarios/cadastro/', views.cadastro, name='cadastro'),
    path('usuarios/cadastro/submit', views.cadastro),
    #url(r'^cadstro$', views.cadastro, name='cadastro')
    #url(r'^', include('projeto_django.urls', namespace='usuarios', app_name='projeto_django')),
    #path('login/cadastro/', views.cadastro),

    #path('login/cadastro/voltar', views.logout_user),

    #path('account/', include('account.urls')),
    #path('registrar/', views.register.as_view(), name='registrar'),
    #path('registrar/', views.cadastro, name='registrar'),

]
