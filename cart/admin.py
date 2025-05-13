from django.contrib import admin

from cart.models import CartItem, Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total_quantity")

    def total_quantity(self, obj):
        return sum(item.quantity for item in obj.items.all())


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "quantity", "product", "get_product_price", "total_price")

    def get_product_price(self, obj):
        return obj.product.price
    get_product_price.short_description = "Цена продукта"



