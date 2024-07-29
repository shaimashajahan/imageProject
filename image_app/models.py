from django.db import models

# Create your models here.
class Product(models.Model):
    Product_name=models.CharField(max_length=255,null=True)
    Product_price=models.IntegerField(null=True)
    Product_qty=models.IntegerField(null=True)
    image=models.ImageField(upload_to="image/",null=True)
    
