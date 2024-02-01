from django.contrib import admin

# Register your models here.
from .models import Brand, Category, Item, PopularItems, Offer, Firm


#admin.site.register(Brand)
@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    search_fields =['name']

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

@admin.register(PopularItems)
class PopularItemsAdmin(admin.ModelAdmin):
    list_display =('item', 'validity_date',)
    search_fields =['item__name','item__code']

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display =('description', 'validity_date',)
    search_fields =['description','validity_date']