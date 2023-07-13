from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View


from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import User

# Create your views here.

class UserBaseView(View):
    template_name = 'user.html'
    model = User
    fields = '__all__'
    success_url = reverse_lazy('user:all')

class UserListView(UserBaseView,ListView):
    
    """
    ESTO ME PERMITE CREAR UNA VISTA 
    """

class UserDetailView(UserBaseView,DetailView):
    template_name = "user_detail.html"

class UserCreateView(UserBaseView,CreateView):
    template_name = "user_create.html"
    extra_context = {
        "tipo": "Crear usuario"
    }

class UserUpdateView(UserBaseView,UpdateView):
    template_name = "user_create.html"
    extra_context = {
        "tipo": "Actualizar usuario"
    }

class UserDeleteView(UserBaseView,DeleteView):
    template_name = "user_delete.html"
    extra_context = {
        "tipo": "Borrar usuario"
    }