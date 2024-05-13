from django.db import models
import uuid
# DRY= do not repeat yourself
# Create your models here

class basemodel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4 ,editable= False ,primary_key= True)
    created_at = models.DateField(auto_created= True)
    update_at = models.DateField(auto_created=True)

    class Meta:
        abstract = True
class Products(basemodel):
    product_name = models.CharField(max_length=100)
    product_slug = models.SlugField(unique=True)
    product_description =models.TextField()
    product_price = models.IntegerField(default=0)
    product_demo_prise = models.IntegerField(default=0)



class ProductmetaInformation(basemodel):
    product= models.OneToOneField(Products ,on_delete= models.CASCADE)
    product_measuring = models.CharField(max_length=100 , choices=(("KG","KG") ,("ML","ML" ,),("L","L") ,(None,None)))
    product_quantity = models.CharField(max_length=50, null=True, blank=True)

    
class ProductImages(basemodel):
    product_images = models.ImageField(upload_to = "Products")