from django.shortcuts import render, get_object_or_404
from .models import Category, Recipe

def main(request):
    # Головна сторінка, наприклад, показує всі категорії
    categories = Category.objects.all()
    return render(request, 'main.html', {'categories': categories})

def category_list(request):
    # Список усіх категорій
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def recipe_list(request):
    # Список усіх рецептів
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})

