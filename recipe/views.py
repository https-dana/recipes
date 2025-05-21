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
        category_name = Category.objects.get(id=category_id).name
    else:
        recipes = Recipe.objects.all()
        category_name = None
    return render(request, 'recipe/recipe_list.html', {'recipes': recipes, 'category_name': category_name})
