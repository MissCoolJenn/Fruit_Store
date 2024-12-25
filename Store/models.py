from django.contrib.auth.models import AbstractUser
from django.db import models

def return_name(instance):
    return instance.name

# Можно использовать как и просто Фрукты так и Боксы
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    sostav = models.TextField(blank=True)
    amount = models.CharField(max_length=15)
    price = models.IntegerField()
    image = models.ImageField()
    awailable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Данные пользователя
class CustomUser(AbstractUser):
    name = models.CharField(max_length=30, unique=True)
    address = models.CharField(blank=True, max_length=250)
    nickname_tg = models.CharField(blank=True, max_length=50, unique=True)
    telephone = models.CharField(max_length=15, blank=True, unique=True)
    
    def __str__(self):
        return self.name

# Список оформленных заказов
class Order(models.Model):
    user_pk = models.ForeignKey(CustomUser, on_delete=models.SET(return_name))
    order_list = models.TextField()
    status = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
    #    return self.pk


# Список отзывов
class Feedback(models.Model):
    product_pk = models.ForeignKey(Product, on_delete=models.SET(return_name))
    user_pk = models.ForeignKey(CustomUser, on_delete=models.SET(return_name))
    review = models.IntegerField()
    text = models.TextField(blank=True, max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
