from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from datetime import date
from django.utils import timezone
from .models import Brand, Category, Item, PopularItems, Offer, Firm
import re
# Create your views here.
rooms =[
    {'id':1, 'name':'let learn python'},
    {'id':2, 'name':'Design the world'},
    {'id':3, 'name':'make the world better'}
]

def home(request):
    if is_mobile(request):
        company = Firm.objects.first()
        brands = Brand.objects.all().order_by('-updated')
        categories = Category.objects.all().order_by('-updated')[:6]
        items = Item.objects.all().order_by('-created')[:4]
        popular_items = PopularItems.objects.filter(validity_date__gte=date.today())
        current_date = timezone.now().date()
        star_offer = Offer.objects.filter(
            is_star_offer=True, 
            validity_date__gte=current_date
        ).order_by('-updated').first()
        offers = Offer.objects.filter(
            validity_date__gte=current_date
        ).order_by('-updated')
        
        context ={'company':company, 'brands':brands, 'categories':categories,'items':items, 'popular_items':popular_items,
                'star_offer': star_offer,'offers':offers}
        return render(request, 'pages/pages/home.html', context)
        pass
    else:
        return render(request, 'base/room.html')
        # Handle PC-specific logic
        pass
    



def room(request,pk):
    room = None
    for i in rooms: 
        if i['id'] == int(pk):
            room = i
    context ={'room':room}
    return render(request, 'base/room.html',context)

def brand_categories(request):
    brand_id = request.GET.get('_id', None)
    if brand_id:
        brand = Brand.objects.get(id=brand_id)
        brand_cat = brand.category_set.all()
        brands = Brand.objects.all()
        context ={'brand':brand ,'brand_cat':brand_cat, 'brands':brands}
    else:
        context= {}
    return render(request, 'pages/pages/categories.html',context)

def Category_items(request):
    category_id = request.GET.get('_id',None)
    if category_id:
        category = Category.objects.get(id = category_id)
        cat_items = category.item_set.all()
        # q = request.GET.get('q') if request.GET.get('q') != None else ''
        # items = Item.objects.filter(
        #     Q(code__icontains=q) |
        #     Q(name__icontains=q) |
        #     Q(description__icontains=q)
        # )
        context = {'category':category, 'cat_items':cat_items}
    else:
        context={}
    
    return render(request,'pages/components/post-list.html',context)

def item(request):
    item_id = request.GET.get('_id', None)
    if item_id:
        item = Item.objects.get(id=item_id)
        context ={'item':item }
    else:
        context= {}

    return render(request, 'pages/pages/item.html',context)

def offer(request):
    offer_id = request.GET.get('_id', None)
    if offer_id:
        offer = Offer.objects.get(id=offer_id)
        context ={'offer':offer }
    else:
        context= {}

    return render(request, 'pages/pages/offer.html',context)

def categories(request):
    offer_id = request.GET.get('_id', None)
    categories = Category.objects.all().order_by('-updated')
    
    context= {'categories':categories}

    return render(request, 'pages/pages/categories-list.html',context)

def is_mobile(request):
    """Simple detection of mobile devices."""
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    mobile_browser_patterns = [
        'mobile', 'android', 'silk/', 'kindle', 'blackberry', 'opera mobile',
        'windows phone', 'windows mobile', 'fennec', 'iphone', 'ipod', 'ipad'
    ]
    return any(pattern in user_agent for pattern in mobile_browser_patterns)