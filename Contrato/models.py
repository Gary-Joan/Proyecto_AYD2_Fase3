from django.db import models
from Menu.models import Menu
from Montaje.models import Montaje
from Restaurante.models import Restaurante
from Salon.models import Salon
from User.models import User

# Create your models here.
class Contrato(models.Model):
    Cliente = models.ForeignKey(User, on_delete=True, related_name='Cliente')
    Gerente = models.ForeignKey(User, on_delete=True, related_name='Gerente')
    Menu = models.ManyToManyField(Menu, through='Contrato_Menu')
    Montaje = models.ForeignKey(Montaje, on_delete=True, related_name='Montaje')
    Restaurante = models.ForeignKey(Restaurante, on_delete=True, related_name='Restaurante')
    Salon = models.ForeignKey(Salon, on_delete=True, related_name='Salon')

class Contrato_Menu(models.Model):
    Menu = models.ForeignKey(Menu, on_delete=True, related_name='MenuContrato')
    Contrato = models.ForeignKey(Contrato, on_delete=True, related_name='ContratoMenu')
    Cantidad = models.IntegerField(default=1)