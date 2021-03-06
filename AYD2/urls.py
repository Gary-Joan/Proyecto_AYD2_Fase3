"""AYD2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from Contrato.views import ContratoView, DeleteContratoView, ContratoNewView
from Ingrediente.views import IngredienteView, DeleteIngredienteView, IngredienteNewView
from Menu.views import MenuView, DeleteMenuView, MenuNewView, MenuIngredienteNewView
from Montaje.views import MontajeView, DeleteMontajeView, MontajeNewView
from Restaurante.views import RestauranteView, DeleteRestauranteView, RestauranteNewView
from Salon.views import SalonView, DeleteSalonView, SalonNewView
from User.views import index

urlpatterns = [

    #url(r'', include('Restaurante.urls')),
    path('admin/', admin.site.urls),
    url(r'^silk/', include('silk.urls', namespace='silk')),
    #/
    path('', index, name='index'),
    #Contrato
    path('Contrato/', ContratoView.as_view(), name='contrato'),
    path('Contrato/Delete/', DeleteContratoView.as_view(), name='delete_contrato'),
        #Con frontend
    path('Contrato/all/', ContratoNewView, name='all_contrato'),
    #Ingrediente
    path('Ingrediente/', IngredienteView.as_view(), name='ingrediente'),
    path('Ingrediente/Delete/', DeleteIngredienteView.as_view(), name='delete_ingrediente'),
        #Con frontend    
    path('Ingrediente/all/', IngredienteNewView.as_view(), name='all_ingrediente'),
    #Menu
    path('Menu/', MenuView.as_view(), name='menu'),
    path('Menu/Delete/', DeleteMenuView.as_view(), name='delete_menu'),
        #Con frontend
    path('Menu/all/', MenuNewView, name='all_menu'),
    path('Menu/ingrediente/all',MenuIngredienteNewView, name="all_menu_ingrediente"),
    #Montaje
    path('Montaje/', MontajeView.as_view(), name='montaje'),
    path('Montaje/Delete/', DeleteMontajeView.as_view(), name='delete_montaje'),
        #Con frontend
    path('Montaje/all/', MontajeNewView, name='all_montaje'),
    #Restaurante
    path('Restaurante/', RestauranteView.as_view(), name='restaurante'),
    path('Restaurante/Delete/', DeleteRestauranteView.as_view(), name='delete_restaurante'),
        #Con frontend    
    path('Restaurante/all/', RestauranteNewView.as_view(), name='all_restaurant'),
    #Salon
    path('Salon/', SalonView.as_view(), name='salon'),
    path('Salon/Delete/', DeleteSalonView.as_view(), name='delete_salon'),
        #Con frontend
    path('Salon/all/', SalonNewView, name='all_salon'),
    #User
    #url(r'^rest-auth/', include('rest_auth.urls'))
  
]
