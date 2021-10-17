from django.db import models

# Create your models here.

class Electronic(models.Model):

    title = models.CharField(max_length=20)
    content = models.TextField()
    data_published= models.DateTimeField(auto_now_add=True)

class Product(models.Model):

    name=models.CharField(max_length=150)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):

    name =models.CharField(max_length=150)
    brand = models.TextField()

    def __str__(self):
        return self.name