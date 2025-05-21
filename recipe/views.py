from django.shortcuts import render
from .models import Category, Recipe 

def main(request):
    categories = Category.objects.all()
    return render(request, 'main.html', context={'categories': categories})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'recipe/category_list.html', {'categories': categories})

def recipe_list(request, category_id=None):
    if category_id:
        recipes = Recipe.objects.filter(category_id=category_id)
    else:
        recipes = Recipe.objects.all()
    return render(request, 'recipe/recipe_list.html', {'recipes': recipes})
