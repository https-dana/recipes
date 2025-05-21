import pytest
from django.utils import timezone
from recipe.models import Category, Recipe

@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(name="Desserts")
    assert category.name == "Desserts"
    # Перевірка __str__ якщо є (якщо ні — можна пропустити)
    assert str(category) == "Desserts"

@pytest.mark.django_db
def test_category_iter_method():
    category = Category.objects.create(name="Drinks")
    items = list(category)  # викликаємо __iter__
    # Тобі потрібно визначити, що повертає __iter__ — наприклад, список з name
    # Припустимо __iter__ повертає ітератор по словах назви
    assert items == list("Drinks")  # або підкоригуй під свою реалізацію

@pytest.mark.django_db
def test_create_recipe_with_category():
    category = Category.objects.create(name="Main course")
    recipe = Recipe.objects.create(
        title="Borscht",
        description="Traditional Ukrainian soup",
        instructions="Cook beets, add broth, simmer.",
        ingredients="Beets, potatoes, cabbage, broth",
        created_at=timezone.now(),
        updated_at=timezone.now(),
        category=category
    )
    assert recipe.title == "Borscht"
    assert recipe.category == category

@pytest.mark.django_db
def test_recipe_str_and_fields():
    category = Category.objects.create(name="Salads")
    recipe = Recipe.objects.create(
        title="Greek Salad",
        description="Fresh and tasty",
        instructions="Mix all ingredients and dress with olive oil.",
        ingredients="Tomatoes, cucumbers, olives, feta cheese",
        created_at=timezone.now(),
        updated_at=timezone.now(),
        category=category
    )
    assert recipe.title == "Greek Salad"
    assert "tomatoes" not in recipe.ingredients.lower()  # тут перевірка що немає помилки (можеш підкоригувати)
    # Перевірка рядкового представлення (якщо є __str__)
    # assert str(recipe) == "Greek Salad"  # якщо реалізовано

