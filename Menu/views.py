from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Menu, Menu_Ingrediente
from .serializers import MenuSerializer
from rest_framework import status

from .forms import MenuForm, MenuIngredienteForm

# Create your views here.
class MenuView(APIView):
    permission_classes = []

    def get(self, request):
        id = request.data['Menu']
        queryset = Menu.objects.get(id=id)
        serializer = MenuSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        nombre = request.data['Nombre']
        descripcion = request.data['Descripcion']
        precio = request.data['Precio']        
        queryset = Menu(Nombre=nombre, Descripcion=descripcion, Precio=precio)
        queryset.save()
        serializer = MenuSerializer(queryset, many = False, context={'request': request})
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

class DeleteMenuView(APIView):
    permission_classes = []

    def post(self, request):
        id = request.data['Menu']
        queryset = Menu.objects.get(id=id)
        queryset.delete()
        return Response(status=status.HTTP_200_OK)

def MenuNewView(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
    form = MenuForm()
    queryset = Menu.objects.filter()
    return render(request, 'menu.html', {'form': form,'object_list':queryset})

def MenuIngredienteNewView(request):
    if request.method == "POST":
        form = MenuIngredienteForm(request.POST)
        if form.is_valid():
            menu_ingrediente = form.save(commit=False)
            menu_ingrediente.save()
    form = MenuIngredienteForm()
    queryset = Menu_Ingrediente.objects.filter()
    return render(request, 'menu_ingrediente.html', {'form': form,'object_list':queryset})