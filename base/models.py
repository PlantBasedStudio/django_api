from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    numReviews = models.IntegerField()
    
