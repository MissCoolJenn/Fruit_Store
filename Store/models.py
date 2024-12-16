from django.db import models

def return_name(instance):
    return instance.name

# Можно использовать как и просто Фрукты так и Боксы
class Product(models.Model):
    name = models.CharField(null=False, max_length=50)
    description = models.TextField(null=False)
    sostav = models.TextField(null=True)
    amount = models.CharField(null=False, max_length=15)
    price = models.IntegerField(null=False)
    image = models.ImageField(null=False)
    awailable = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name

# Данные пользователя
class User(models.Model):
    name = models.CharField(null=False, max_length=30)
    address = models.CharField(null=True, max_length=250)
    nickname_tg = models.CharField(null=True, max_length=50)
    telephone = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name

# Список оформленных заказов
class Order(models.Model):
    user_pk = models.ForeignKey(User, on_delete=models.SET(return_name))
    order_list = models.TextField(null=False)
    status = models.CharField(null=False, max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
    #    return self.pk

# Список отзывов
class Feedback(models.Model):
    product_pk = models.ForeignKey(Product, on_delete=models.SET(return_name))
    user_pk = models.ForeignKey(User, on_delete=models.SET(return_name))
    review = models.IntegerField(null=False)
    text = models.TextField(null=True, max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
