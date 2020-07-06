#Tamilly's code / 2020-01-07

from django.db import models
from django.conf import settings
from django.utils import timezone

class User(models.Model):
	cpf = models.BigIntegerField(primary_key=True)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	birth_date = models.DateField(auto_now=False, auto_now_add=False)
	password = models.CharField(max_length=20)
	admin = models.BooleanField()
	
	def add_user(self):
		self.save()
	
	def __str__(self):
		return self.name


class Product(models.Model): # Model definition
	# Attributes type definition	
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	bar_code = models.IntegerField()
	name = models.CharField(max_length=100)
	description = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	price = models.DecimalField(max_digits=10, decimal_places=3)	

	categories = models.TextChoices('Categoria', 'BELEZA LIMPEZA ALIMENTO CASA OUTROS')	

	category = models.CharField(blank=True, choices=categories.choices, max_length=10)
	validity = models.DateField(auto_now=False, auto_now_add=False)

	# Methods definition

	def add_product(self): 
		self.created_date = timezone.now()
		self.save()

	def __str__(self): 
		return self.name


