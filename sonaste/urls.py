"""
URL configuration for sonaste project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path , include

from .views import HomeView, MusicaView, NovedadesView, ContactoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name = 'home_page'),
    path('Musica', MusicaView.as_view(), name = 'musica_page'),
    path('Novedades', NovedadesView.as_view(), name = 'novedades_page'),
    path('Contacto', ContactoView.as_view(), name = 'contacto_page'),
    path('artist/', include('app_sonaste.urls'))
]
