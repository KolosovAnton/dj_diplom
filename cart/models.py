from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


# заказы
class Order(models.Model):
    order_id = models.CharField(
        max_length=50,
        verbose_name='ID заказа'
    )
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    quantity_item = models.IntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name='Количество товаров'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.client}'


# товары в заказе
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order_items'
    )
    quantity = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.order}'
