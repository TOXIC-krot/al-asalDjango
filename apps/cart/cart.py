from django.conf import settings
from apps.products.models import Product


class Cart(object):

    def __init__(self, request):
        """
        Initializing the cart
        """
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            # save an empty cart in the session
            cart = self.session["cart"] = {}
        self.cart = cart

    @property
    def total_count(self):
        """
        Counting all items in cart.
        """
        return len(self.cart)

    @property
    def total_price(self):
        """
        Calculating the cost of goods in the cart.
        """
        return sum(int(item["price"]) * item["quantity"] for item in self.cart.values())

    def add(self, product, quantity=1):
        """
        Add a product to your cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0, "price": str(product.price)}
        
        self.cart[product_id]["quantity"] += quantity
        if self.cart[product_id]["quantity"] <= 0:
            self.remove(product)
            return
        self.save()

    def remove(self, product):
        """
        Removing an item from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        # Updating the cart session
        self.session["cart"] = self.cart
        # Mark the session as "modified" to ensure it is saved
        self.session.modified = True

    def __iter__(self):
        """
        Iterate through items in cart and retrieve products from database.
        """
        product_ids = self.cart.keys()
        # getting product objects and adding them to cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]["product"] = product

        for item in self.cart.values():
            item["price"] = int(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def clear(self):
        '''
        Removing the cart from session.
        '''
        del self.session["cart"]
        self.session.modified = True
