from django.views.generic import  TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

class MusicaView(TemplateView):
    template_name = 'musica.html'

class NovedadesView(TemplateView):
    template_name = 'novedades.html'

class ContactoView(TemplateView):
    template_name = 'contacto.html'