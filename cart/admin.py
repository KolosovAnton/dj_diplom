from django.contrib import admin
from cart.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'quantity_item', 'created_at')
    list_filter = ('client', 'created_at')
    search_fields = ('client', 'created_at')
    ordering = ('-created_at',)
    inlines = (OrderItemInline,)


admin.site.register(Order, OrderAdmin)
