from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .apps import CatalogConfig
from catalog.views import SubCategoryViewSet, ProductViewSet, CategoryViewSet

app_name = CatalogConfig.name

router = SimpleRouter()
router.register(r"subcategory", SubCategoryViewSet)
router.register(r"product", ProductViewSet)
router.register(r"category", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += router.urls
