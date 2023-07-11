from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Artist

# Create your views here.


class ArtistBaseView(View):
    template_name = 'artist.html'
    model = Artist
    fields = '__all__'
    success_url = reverse_lazy('atist:all')


class ArtistListView(ArtistBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS VINOS
    """

class ArtistDetailView(ArtistBaseView,DetailView):
    template_name = "artist_detail.html"

class ArtistCreateView(ArtistBaseView,CreateView):
    template_name = "artist_create.html"
    extra_context = {
        "tipo": "Crear artista"
    }

class ArtistUpdateView(ArtistBaseView,UpdateView):
    template_name = "artist_create.html"
    extra_context = {
        "tipo": "Actualizar artista"
    }

class ArtistDeleteView(ArtistBaseView,DeleteView):
    template_name = "artist_delete.html"
    extra_context = {
        "tipo": "Borrar artista"
    }
