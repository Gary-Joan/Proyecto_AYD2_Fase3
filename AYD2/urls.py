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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    #Contrato
    path('Contrato/', ContratoView.as_view(), name='contrato'),
    path('Contrato/Delete/', DeleteContratoView.as_view(), name='delete_contrato'),
    #Ingrediente
    path('Ingrediente/', IngredienteView.as_view(), name='ingrediente'),
    path('Ingrediente/Delete/', DeleteIngredienteView.as_view(), name='delete_ingrediente'),
    #Menu
    path('Menu/', MenuView.as_view(), name='menu'),
    path('Menu/Delete/', DeleteMenuView.as_view(), name='delete_menu'),
    #Montaje
    path('Montaje/', MontajeView.as_view(), name='montaje'),
    path('Montaje/Delete/', DeleteMontajeView.as_view(), name='delete_montaje'),
    #Restaurante
    path('Restaurante/', RestauranteView.as_view(), name='restaurante'),
    path('Restaurante/Delete/', DeleteRestauranteView.as_view(), name='delete_restaurante'),
    #Salon
    path('Salon/', SalonView.as_view(), name='salon'),
    path('Salon/Delete/', DeleteSalonView.as_view(), name='delete_salon'),
]
