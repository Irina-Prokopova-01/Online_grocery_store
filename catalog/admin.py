from django.contrib import admin

from catalog.models import SubCategory, Category, Product


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """
    Админ. интерфейс для модели SubCategory.
    Этот класс определяет, какие поля будут отображаться в списке подкатегорий
    в административной панели Django. Позволяет управлять подкатегориями через
    интерфейс администратора.
    """

    list_display = ("id", "title", "description", "category", "slug", "image")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Админ. интерфейс для модели Category.
    Этот класс определяет, какие поля будут отображаться в списке категорий
    в административной панели Django. Позволяет управлять категориями через
    интерфейс администратора.
    """

    list_display = ("id", "title", "description", "slug", "image")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Админ. интерфейс для модели Product.
    Этот класс определяет, какие поля будут отображаться в списке продуктов
    в административной панели Django. Позволяет управлять продуктами через
    интерфейс администратора.
    """

    list_display = (
        "id",
        "name",
        "description",
        "slug",
        "category",
        "subcategory",
        "price",
        "image_small",
        "image_medium",
        "image_large",
    )
