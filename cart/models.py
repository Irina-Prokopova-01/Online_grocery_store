from users.models import User
from django.db import models
from catalog.models import Product


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # def total_quantity(self, obj):
    #     return sum(item.quantity for item in obj.items.all())

    def __str__(self):
        return f"Корзина {self.user.email}"

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} (x{self.quantity}) - {self.product.price * self.quantity}₽"

    class Meta:
        verbose_name = "Элемент корзины"
        verbose_name_plural = "Элементы корзины"


