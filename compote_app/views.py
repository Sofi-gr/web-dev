from django.shortcuts import render
from rest_framework import viewsets
from .models import Fruit, Ingredient, Compote
from .serializers import FruitSerializer, IngredientSerializer, CompoteSerializer

class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class CompoteViewSet(viewsets.ModelViewSet):
    queryset = Compote.objects.all()
    serializer_class = CompoteSerializer

