from django.db import models


	

class Book(models.Model):
	author = models.CharField(max_length=100)
	Book_name = models.CharField(max_length=10)
	isbn = models.CharField(max_length=20)
	desp = models.CharField(max_length=100)

class Post(models.Model):
	author = models.CharField(max_length=250)
	age = models.CharField(max_length=10)
	gender = models.CharField(max_length=500)
	Born_in = models.CharField(max_length=250)
	abt_author = models.CharField(max_length=1000)

			

# Create your models here.