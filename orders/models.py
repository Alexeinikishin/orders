from django.db import models
from django.urls import reverse

class Order(models.Model):
	customer = models.CharField(max_length=200)
	task = models.TextField()
	price = models.IntegerField()

	def __str__(self):
		return self.customer

	def get_absolute_url(self):
		return reverse("order_detail", kwargs={"pk": self.pk})
		