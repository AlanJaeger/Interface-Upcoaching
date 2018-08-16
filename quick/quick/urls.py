"""quick URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from index.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    url(r'^index/$', DashboardView.as_view(), name='index'),
    url(r'^professor/$', DashboardProfessor.as_view(),name = 'professor') ,
    url(r'admin/', admin.site.urls),
    #path('index/', index)
    #path('/', professor)
    url(r'administrador',DashboardAdm.as_view()),
    url(r'pedidos',DashboardPedidos.as_view(), name = 'pedidos'),
    url(r'aluno',DashboardAluno.as_view()),
    url(r'aprovar/(?P<id_candidato>\d+)/',AprovarEntrada.as_view(), name = 'aprovar'),
    url(r'update',UpdateImagem.as_view(), name = 'update'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^curso/$', Curso.as_view(), name='curso'),
    url(r'^catalogo/$', CatalogoProfessor.as_view(), name='catalogo')
        
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)