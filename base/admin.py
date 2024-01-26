from django.contrib import admin

# Register your models here.
from .models import Brand, Category, Item


#admin.site.register(Brand)
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields =['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =('name', 'brand', 'description')
    search_fields =['name','brand__name']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display =('code', 'name','category')
    search_fields =['code','name']