from django.shortcuts import render, get_object_or_404
from .models import Category, Recipe

def main(request):
    categories = Category.objects.all()
    return render(request, 'main.html', {'categories': categories})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})

def recipe_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'recipes_by_category.html', {'category': category, 'recipes': recipes})
