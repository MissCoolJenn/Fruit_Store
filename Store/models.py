from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    #game = models.CharField(max_length=50)
    #img = models.ImageField(upload_to='media/images/')
    #description = models.TextField()

    def __str__(self):
        return self.title