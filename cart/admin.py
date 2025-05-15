from django.contrib import admin

from cart.models import CartItem, Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Админ. интерфейс для модели Cart (Корзина).
    Позволяет управлять корзинами пользователей в админке Django.
    Отображает идентификатор, пользователя и общее количество товаров в корзине.
    """

    list_display = ("id", "user", "total_quantity")

    def total_quantity(self, obj):
        return sum(item.quantity for item in obj.items.all())


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """
    Админ. интерфейс для модели CartItem (Элемент корзины).
    Позволяет управлять элементами корзины в админке Django.
    Отображает идентификатор, корзину, количество, продукт,
    цену продукта и общую стоимость элемента корзины.
    """

    list_display = (
        "id",
        "cart",
        "quantity",
        "product",
        "get_product_price",
        "total_price",
    )

    def get_product_price(self, obj):
        return obj.product.price

    get_product_price.short_description = "Цена продукта"
