from rest_framework import serializers
from catalog.models import Category, SubCategory, Product


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)

    def create(self, validation_data):
        subcategories_data = validation_data.pop("subcategories")
        subcategories = [SubCategory.objects.create(**subcat_data) for subcat_data in subcategories_data]
        category = Category.objects.create(**validation_data)
        category.subcategories.set(subcategories)  # Установка подкатегорий для категории
        return category

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

