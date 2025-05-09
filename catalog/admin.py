from django.contrib import admin

from catalog.models import SubCategory, Category, Product


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "category", "slug", "image")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "slug", "image")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "slug", "category", "subcategory", "price", "image_small", "image_medium", "image_large")

