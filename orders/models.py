from django.db import models
from bock.models import Product
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator


class order(models.Model):
	first_name = models.CharField(max_length=50, verbose_name=("förnamn"))
	last_name = models.CharField(max_length=50, verbose_name=("efternamn"))
	email = models.EmailField()

	address = models.CharField(max_length=250, verbose_name=("adress"))
	postal_code = models.CharField(max_length=50, verbose_name=("postnummer"))
	city = models.CharField(max_length=100, verbose_name=("stad"))
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False, verbose_name=("betalas"))
	Phone_number = models.CharField(max_length=50, verbose_name=("Telefonnummer"))

	class Meta:
		ordering = ('-created',)
		verbose_name = "order"
		verbose_name_plural = "orders"

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		total_cost = sum(item.get_cost() for item in self.items.all())
		return total_cost - total_cost * (self.discount / Decimal('100'))


class OrderItem(models.Model):
	order = models.ForeignKey(
		order, related_name='items', on_delete=models.CASCADE)
	product = models.ForeignKey(
		Product, related_name='order_items', on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	class Meta:
		verbose_name = "OrderItem"
		verbose_name_plural = "OrderItems"

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity
