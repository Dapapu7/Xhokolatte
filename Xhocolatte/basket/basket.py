from decimal import Decimal

from django.conf import settings

from XhocolatteApp.models import Product
from checkout.models import DeliveryOptions


class Basket():
    """
        A base Basket class, providing some default behaviors 
        that can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')

        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty):
        """
            Adding and updating the users basket session data
        """
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {'precio': str(product.regular_price), 'qty': qty}

        self.save()

    def delete(self, product):
        """
            Delete item from session data
        """
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]

        self.save()

    def update(self, product, qty):
        """
            Update item from seesion data
        """
        product_id = str(product)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty

        self.save()

    def __iter__(self):
        """
            Collect the product_id in the session data to query the database
            and return products
        """
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['precio'] = Decimal(item['precio'])
            item['precio_total'] = item['precio'] * item['qty']
            yield item

    def __len__(self):
        """
            Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values()) 

    def get_subtotal_price(self):
        return sum(Decimal(item["precio"]) * item["qty"] for item in self.basket.values())

    def get_delivery_price(self):
        newprice = 0.00

        if "purchase" in self.session:
            newprice = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price

        return newprice

    def get_total_price(self):
        newprice = 0.00
        subtotal = sum(Decimal(item["precio"]) * item["qty"] for item in self.basket.values())

        if "purchase" in self.session:
            newprice = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price

        total = subtotal + Decimal(newprice)
        return total

    def basket_update_delivery(self, deliveryprice=0):
        subtotal = sum(Decimal(item["precio"]) * item["qty"] for item in self.basket.values())
        total = subtotal + Decimal(deliveryprice)
        return total

    def clear(self):
        del self.session["skey"]
        del self.session["address"]
        del self.session["purchase"]
        self.save()

    def save(self):
        self.session.modified = True

    