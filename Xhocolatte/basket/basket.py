from decimal import Decimal

from XhocolatteApp.models import Product
from checkout.models import DeliveryOptions


class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')

        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty):
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {'precio': str(product.regular_price), 'qty': qty}

        self.save()

    def delete(self, product):
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]

        self.save()

    def update(self, product, qty):
        product_id = str(product)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty

        self.save()

    def __iter__(self):
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

    