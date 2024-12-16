from django.contrib import admin
from .models import Product, User, Order, Feedback

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'sostav', 'amount', 'price', 'image', 'awailable')

class UsersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_pk', 'order_list', 'status', 'date')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_pk', 'user_pk', 'review', 'text', 'date')

admin.site.register(Product, ProductsAdmin)
admin.site.register(User, UsersAdmin)
admin.site.register(Order, OrdersAdmin)
admin.site.register(Feedback, FeedbackAdmin)