from rest_framework import serializers
from catalog.models import Category, SubCategory, Product


class SubCategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели SubCategory.
    Используется для преобразования данных подкатегорий в формат JSON и обратно.
    Позволяет выполнять операции сериализации и десериализации для подкатегорий.
    """

    class Meta:
        model = SubCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Category.
    Используется для преобразования данных категорий в формат JSON и обратно.
    Позволяет создавать категории вместе с подкатегориями.
    """

    subcategories = SubCategorySerializer(many=True)

    def create(self, validation_data):
        subcategories_data = validation_data.pop("subcategories")
        subcategories = [
            SubCategory.objects.create(**subcat_data)
            for subcat_data in subcategories_data
        ]
        category = Category.objects.create(**validation_data)
        category.subcategories.set(
            subcategories
        )  # Установка подкатегорий для категории
        return category

    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.
    Используется для преобразования данных продуктов в формат JSON и обратно.
    Позволяет выполнять операции сериализации и десериализации для продуктов.
    """

    class Meta:
        model = Product
        fields = "__all__"
