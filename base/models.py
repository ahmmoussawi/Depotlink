from django.db import models
from datetime import date

# Create your models here.
class Firm(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True,upload_to='brands/', default='defaultbrand.png')

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True,upload_to='brands/', default='defaultbrand.png')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Category(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(null=True,blank=True,upload_to='categories/',default='defaultcategory.png')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.name} - {self.brand.name}"

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField(null= True)
    hscode = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True,blank=True,upload_to='items/',default='defaultitem.png')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.code} - {self.name}"
    
class PopularItems(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    validity_date = models.DateField()

    def is_valid(self):
        return date.today() <= self.validity_date
    
class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='offers/',default='defaultbrand.png') 
    is_star_offer = models.BooleanField(default=False)
    validity_date = models.DateField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True)

    def is_valid(self):
        return date.today() <= self.validity_date