from rest_framework import viewsets, status

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from rest_framework.exceptions import PermissionDenied, NotFound
from .serializers import CartSerializer, CartItemSerializer
from cart.services import add_to_cart


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    queryset = Cart.objects.all()

    def get_object(self):
        # Получаем корзину текущего пользователя или создаем её
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

    def get_queryset(self):
        # Возвращаем корзину только для текущего пользователя
        return Cart.objects.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        # Получаем корзину для текущего пользователя
        try:
            cart = self.get_queryset().get()
            serializer = self.get_serializer(cart)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({"message": "Корзина не найдена."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        # Создаем или получаем корзину для текущего пользователя
        cart, created = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)  # По умолчанию количество 1

        # print(f"Trying to add product_id: {product_id} with quantity: {quantity}")

        if product_id:
            try:
                # Используем сервисную функцию для добавления товара в корзину
                add_to_cart(cart, product_id, quantity)
                return Response({"message": "Товар добавлен в корзину"}, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Товар не найден"}, status=status.HTTP_400_BAD_REQUEST)


    def clear(self, request, *args, **kwargs):
        try:
            cart = self.get_object()
            cart.cartitem_set.all().delete()  # Удаляем все товары из корзины
            return Response({"message": "Корзина очищена."}, status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            return Response({"message": "Корзина не найдена."}, status=status.HTTP_404_NOT_FOUND)



    def destroy(self, request, *args, **kwargs):
        # Удаляем товар из корзины текущего пользователя
        cart = self.get_object()
        product_id = request.data.get("product_id")

        try:
            cart_item = CartItem.objects.get(cart=cart, product__id=product_id)
            cart_item.delete()
            return Response({"message": "Товар удален из корзины"}, status=status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            return Response({"message": "Товар не найден в корзине"}, status=status.HTTP_404_NOT_FOUND)


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    queryset = CartItem.objects.all()

    def get_queryset(self):
        # Возвращаем элементы корзины только для текущего пользователя
        return CartItem.objects.filter(cart__user=self.request.user)

    def get_object(self):
        # Получаем товар по ID из URL с фильтрацией по текущему пользователю
        obj = super().get_object()
        if obj.cart.user != self.request.user:
            raise PermissionDenied("У вас нет доступа к этому элементу корзины.")
        return obj

    def perform_create(self, serializer):
        try:
            cart = Cart.objects.get(user=self.request.user)
        except Cart.DoesNotExist:
            raise NotFound("Корзина не найдена.")
        serializer.save(cart=cart)
