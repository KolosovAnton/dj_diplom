from django.contrib.auth.models import User
from cart.cart import Cart
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from cart.models import Order, OrderItem
from shop.models import Product


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product, quantity=1)
    return redirect('cart_detail')


def cart_detail(request):
    context = {}
    cart = Cart(request)
    cart_dict = request.session.get('cart')
    list_cart = []
    for key, value in cart_dict.items():
        cart_item = {}
        cart_item['name'] = Product.objects.get(id=int(key))
        cart_item['quantity'] = value['quantity']
        list_cart.append(cart_item)
    if request.method == 'POST':
        user_id = request.user.id
        client = User.objects.get(id=user_id)
        quantity_item = cart.__len__()
        if Order.objects.only('id'):
            order_id = Order.objects.order_by('-id').first().id
        else:
            order_id = 0
        order = Order.objects.create(
            order_id=(order_id+1),
            client=client,
            quantity_item=quantity_item
        )
        for item in list_cart:
            OrderItem.objects.create(
                order=order,
                product=item['name'],
                quantity=item['quantity']
            )
        cart.clear()
        return redirect('home')
    context['cart_len'] = cart.__len__()
    context['cart'] = list_cart
    return render(request, 'shop/cart.html', context)
