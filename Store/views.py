from django.views.generic import ListView
from .models import Product

class HomePage(ListView):
    model = Product
    #ordering = ['title']
    title = 'Fruit Store'
    template_name = 'home.html'