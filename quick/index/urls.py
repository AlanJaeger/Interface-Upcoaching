from django.urls import path, reverse_lazy
from .views import Cadastro
from django.contrib.auth.views import (
    LoginView, LogoutView

)

urlpatterns = [
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('login/', LoginView.as_view(template_name='index/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
]