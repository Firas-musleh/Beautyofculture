from decimal import Decimal
import decimal
from django.conf import settings
from bock.models import Product


class Cart(object):
	"""docstring for Cart"""

	def __init__(self, request):
		"""initalize the cart"""
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)

		if not cart:
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def add(self, product, quantity=1, update_quantity=False):

		product_id = str(product.id)
		if product_id not in self.cart:
			if product.Discountprice > 0:
					product.price = product.Discountprice
			self.cart[product_id] = {'quantity': 0, 'price':str(product.price),'Frakt':str(product.Frakt)}

		if update_quantity:
			self.cart[product_id]['quantity'] = quantity

		else:
			self.cart[product_id]['quantity'] += quantity

		self.save()

	def save(self):

		self.session[settings.CART_SESSION_ID] = self.cart
		self.session.modified = True

	def remove(self, product):
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	def __iter__(self):

		product_ids = self.cart.keys()

		products = Product.objects.filter(id__in=product_ids)

		for product in products:
			self.cart[str(product.id)]['product'] = product

		for item in self.cart.values():

			item['price'] = Decimal(item['price'])
			item['Frakt'] = Decimal(item['Frakt'])
			item['total_price'] = (item['price'] * item['quantity']) + \
   (item['Frakt'] * item['quantity'])

			yield item

	def __len__(self):
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(Decimal(item['price']) * Decimal(item['quantity']) + Decimal(item['Frakt'] * item['quantity'])for item in self.cart.values())

	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True
