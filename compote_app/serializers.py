from rest_framework import serializers
from .models import Fruit, Ingredient, Compote

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class CompoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compote
        fields = '__all__'