from django.db import models

# Create your models here.

class PizzaShop(models.Model):
    name = models.CharField(max_length=30,verbose_name='Pizza')
    description = models.TextField(verbose_name='description pizza')
    rating = models.FloatField(default=0,verbose_name='rating pizza')
    url = models.URLField(verbose_name='url pizza')

    def __str__(self):
        return self.name

class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop,on_delete=models.CASCADE)
    name = models.CharField(max_length=30,verbose_name='Pizza')
    short_description= models.CharField(max_length=30,verbose_name='short description Pizza')
    price = models.IntegerField(default=0,verbose_name='cena')

    def __str__(self):
        return self.name

class Order(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE,verbose_name='Picca')
    name = models.CharField(max_length=30,verbose_name='Name')
    phone = models.CharField(max_length=30,verbose_name='Phone')
    date = models.DateField(auto_now_add=True,verbose_name='Date')

    
