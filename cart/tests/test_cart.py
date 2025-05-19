import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from cart.models import Cart, CartItem
from catalog.models import Product, Category, SubCategory

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(email="test@example.com", password="12345")


@pytest.fixture
def authenticated_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def cart(user):
    return Cart.objects.create(user=user)


@pytest.fixture
def subcategory(category):
    return SubCategory.objects.create(title="Test SubCategory", slug="test-subcategory", category=category)


@pytest.fixture
def category():
    return Category.objects.create(title="Test Category", slug="test-category")


@pytest.fixture
def product(subcategory):
    return Product.objects.create(
        name="Test Product", price=10, slug="test-product", subcategory=subcategory
    )


def test_retrieve_cart(authenticated_client, cart):
    """Тестирует получение корзины текущего пользователя.
    Проверяет, что запрос к API на получение корзины возвращает статус 200
    и правильный идентификатор корзины.
    """
    response = authenticated_client.get("/cart/cart/retrieve/")

    assert response.status_code == status.HTTP_200_OK
    assert (
        response.data["id"] == cart.id
    )  # Проверяем, что возвращается правильная корзина


def test_create_cart_item(authenticated_client, cart, product):
    """
    Тестирует создание элемента корзины.
    Проверяет, что элемент успешно добавляется в корзину,
    возвращая статус 201 и соответствующее сообщение.
    """
    response = authenticated_client.post(
        "/cart/cart/", {"cart_id": cart.id, "product_id": product.id, "quantity": 1}
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["message"] == "Товар добавлен в корзину"
    assert (
        CartItem.objects.count() == 1
    )  # Проверяем, что элемент был добавлен в корзину


def test_create_cart_item_without_product_id(authenticated_client):
    """
    Тестирует создание элемента корзины без указания идентификатора продукта.
    Проверяет, что запрос возвращает статус 400 и соответствующее сообщение об ошибке.
    """
    response = authenticated_client.post("/cart/cart/", {"quantity": 1})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data["message"] == "Товар не найден"


def test_destroy_cart_item(authenticated_client, cart, product):
    """
    Тестирует удаление элемента из корзины.
    Проверяет, что элемент успешно удаляется из корзины и возвращает статус 200
    с соответствующим сообщением.
    """
    cart_item = CartItem.objects.create(cart=cart, product=product, quantity=1)

    response = authenticated_client.delete(
        "/cart/cart/destroy/", {"product_id": product.id}
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data["message"] == "Товар удален из корзины"
    assert CartItem.objects.count() == 0  # Проверяем, что товар был удален


def test_destroy_nonexistent_cart_item(authenticated_client, cart, product):
    """
    Тестирует попытку удаления несуществующего элемента из корзины.
    Проверяет, что запрос возвращает статус 404 и соответствующее сообщение об ошибке.
    """
    response = authenticated_client.delete(
        "/cart/cart/destroy/", {"product_id": product.id}
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data["message"] == "Товар не найден в корзине"


def test_post_cart_item(authenticated_client, cart, product):
    """
    Тестирует повторное добавление элемента в корзину.
    Проверяет, что элемент успешно добавляется в корзину и возвращает статус 201
    с соответствующим сообщением.
    """
    cart_item = CartItem.objects.create(cart=cart, product=product, quantity=1)

    response = authenticated_client.post("/cart/cart/", {"product_id": product.id})

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["message"] == "Товар добавлен в корзину"
    assert CartItem.objects.count() == 1
