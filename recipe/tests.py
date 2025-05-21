from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Desserts")
        self.assertEqual(str(category), "Desserts")
        self.assertEqual(list(iter(category)), ["Desserts"])

class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Breakfast")

    def test_create_recipe(self):
        recipe = Recipe.objects.create(
            title="Pancakes",
            description="Fluffy pancakes",
            instructions="Mix and fry",
            ingredients="Flour, eggs, milk",
            category=self.category
        )
        self.assertEqual(recipe.title, "Pancakes")
        self.assertEqual(recipe.category.name, "Breakfast")
