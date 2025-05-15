from cart.models import CartItem
from catalog.models import Product


def add_to_cart(cart, product_id, quantity=1):
    """Проверяем, есть ли уже этот товар в корзине. Если элемент уже существует, увеличиваем его количество"""
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise ValueError("Продукт не найден.")

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product, defaults={"quantity": quantity}
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()
