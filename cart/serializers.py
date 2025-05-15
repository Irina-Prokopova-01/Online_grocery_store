from rest_framework import serializers
from cart.models import CartItem, Cart
from catalog.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    """
    Сериализатор для элементов корзины.
    Позволяет преобразовывать объекты CartItem в JSON и обратно.
    Включает информацию о товаре и общей стоимости.
    """

    product = ProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ["id", "cart", "product", "quantity", "total_price"]

    def get_total_price(self, obj):
        return obj.product.price * obj.quantity


class CartSerializer(serializers.ModelSerializer):
    """
    Сериализатор для корзины пользователя.
    Позволяет преобразовывать объекты Cart в JSON и обратно.
    Включает информацию о товарах, их количестве и общей стоимости.
    """

    items = CartItemSerializer(many=True, read_only=True)
    total_items = serializers.SerializerMethodField()
    total_prices = serializers.SerializerMethodField()
    total_names = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "user", "items", "total_items", "total_prices", "total_names"]

    def get_total_items(self, obj):
        return sum(item.quantity for item in obj.items.all())

    def get_total_prices(self, obj):
        return sum(item.product.price * item.quantity for item in obj.items.all())

    def get_total_names(self, obj):
        unique_products = {item.product.id for item in obj.items.all()}
        return len(unique_products)
