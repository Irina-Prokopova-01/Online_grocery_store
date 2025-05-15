from users.models import User
from django.db import models
from catalog.models import Product


class Cart(models.Model):
    """
    Модель для представления корзины пользователя.
    Каждая корзина связана с одним пользователем и содержит
    элементы, которые пользователь добавил в свою корзину.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Корзина {self.user.email}"

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class CartItem(models.Model):
    """
    Модель для представления элемента в корзине.
    Каждый элемент корзины связан с конкретной корзиной и продуктом,
    а также содержит информацию о количестве данного продукта.
    """

    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} (x{self.quantity}) - {self.product.price * self.quantity}₽"

    class Meta:
        verbose_name = "Элемент корзины"
        verbose_name_plural = "Элементы корзины"
