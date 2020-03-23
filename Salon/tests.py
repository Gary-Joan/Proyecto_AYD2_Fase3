from django.test import TestCase
from Salon.models import Salon
# Create your tests here.
class TestSalon(TestCase):
    
    def test_create_salon(self):
        Salon(
            Nombre="salon prueba",
            Descripcion="una descripcion de salon",
            Capacidad=100
        ).save()
        salones = Salon.objects.all()
        salon = Salon.objects.get(id=1)
        self.assertEquals(salones.count(),1)
        self.assertEquals(salon.Nombre,"salon prueba")
