from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    taste = models.CharField(max_length=50)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)

class Compote(models.Model):
    name = models.CharField(max_length=100)
    fruits = models.ManyToManyField(Fruit)
    ingredients = models.ManyToManyField(Ingredient)
    preparation_date = models.DateField()
