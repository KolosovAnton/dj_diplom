class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        """
        Добавить продукт в корзину или обновить его количество
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """
        Обновление сессии cart
        """
        self.session['cart'] = self.cart
        self.session.modified = True

    def __len__(self):
        """
        Подсчет всех товаров в корзине
        """
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Удаление корзины из сессии
        """
        del self.session['cart']
        self.session.modified = True
