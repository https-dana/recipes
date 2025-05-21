from django.contrib import admin
from django.urls import path
from recipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('categories/', views.category_list, name='category_list'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/<int:category_id>/', views.recipe_by_category, name='recipe_by_category'),
]
