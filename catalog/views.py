from rest_framework import viewsets


from catalog.models import Product, Category, SubCategory
from users.permissions import IsActiveUser
from catalog.paginators import CatalogPagination
from catalog.serializers import (
    ProductSerializer,
    CategorySerializer,
    SubCategorySerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    """CRUD для работы с продуктами"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CatalogPagination
    permission_classes = [IsActiveUser]


class CategoryViewSet(viewsets.ModelViewSet):
    """CRUD для работы с категориями"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CatalogPagination
    permission_classes = [IsActiveUser]


class SubCategoryViewSet(viewsets.ModelViewSet):
    """CRUD для работы с субкатегориями"""

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = CatalogPagination
    permission_classes = [IsActiveUser]
