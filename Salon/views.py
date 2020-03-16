from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Salon
from .serializers import SalonSerializer
from rest_framework import status

# Create your views here.
class SalonView(APIView):
    permission_classes = []

    def get(self, request):
        id = request.data['Salon']
        salon = Salon.objects.get(id=id)
        serializer = SalonSerializer(salon, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        nombre = request.data['Nombre']
        descripcion = request.data['Descripcion']
        capacidad = request.data['Capacidad']
        salon = Salon(Nombre = nombre, Descripcion = descripcion, Capacidad = capacidad)
        salon.save()
        serializer = SalonSerializer(salon, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

class DeleteSalonView(APIView):
    permission_classes = []

    def post(self, request):
        id = request.data['Salon']
        salon = Salon.objects.get(id=id)
        salon.delete()
        return Response(status=status.HTTP_200_OK)

