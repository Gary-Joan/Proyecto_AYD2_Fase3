from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Restaurante
from .serializers import RestauranteSerializer
from rest_framework import status



def login(request):
    return render(request, 'login.html', {})

# Create your views here.
class RestauranteView(APIView):
    permission_classes = []

    def get(self, request):
        id = request.data['Restaurante']
        queryset = Restaurante.objects.get(id=id)        
        serializer = RestauranteSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        nombre = request.data['Nombre']
        direccion = request.data['Direccion']
        queryset = Restaurante(Nombre = nombre, Direccion = direccion)        
        queryset.save()
        serializer = RestauranteSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

class DeleteRestauranteView(APIView):
    permission_classes = []

    def post(self, request):
        id = request.data['Restaurante']
        queryset = Restaurante.objects.get(id=id)
        queryset.delete()
        return Response(status=status.HTTP_200_OK)


