from cart.models import CartItem
from catalog.models import Product


def add_to_cart(cart, product_id, quantity=1):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise ValueError("Продукт не найден.")

    # Проверяем, есть ли уже этот товар в корзине
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )

    if not created:
        # Если элемент уже существует, увеличиваем его количество
        cart_item.quantity += quantity
        cart_item.save()

