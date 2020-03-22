from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Ingrediente
from .serializers import IngredienteSerializer
from rest_framework import status

# Create your views here.
class IngredienteView(APIView):
    permission_classes = []

    def get(self, request):
        id = request.data['Ingrediente']
        queryset = Ingrediente.objects.get(id=id)
        serializer = IngredienteSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        nombre = request.data['Nombre']
        descripcion = request.data['Descripcion']        
        queryset = Ingrediente(Nombre=nombre, Descripcion=descripcion)
        queryset.save()
        serializer = IngredienteSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

class DeleteIngredienteView(APIView):
    permission_classes = []

    def post(self, request):
        id = request.data['Ingrediente']
        queryset = Ingrediente.objects.get(id=id)
        queryset.delete()
        return Response(status=status.HTTP_200_OK)