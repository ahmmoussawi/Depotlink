from django.db import models

# Create your models here.
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
    image = models.ImageField(null=True,blank=True,upload_to='categories/',default='defaultbrand.png')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.name} - {self.brand.name}"

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField(null= True)
    image = models.ImageField(null=True,blank=True,upload_to='items/',default='defaultbrand.png')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.code} - {self.name}"