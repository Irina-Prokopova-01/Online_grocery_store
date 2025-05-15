from rest_framework.pagination import PageNumberPagination


class CatalogPagination(PageNumberPagination):
    """Класс для пагинации списка товаров в каталоге. Определяет максимальное количество элементов, которое может
    быть запрошено на одной странице"""

    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 3
