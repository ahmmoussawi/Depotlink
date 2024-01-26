from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Brand, Category, Item
# Create your views here.
rooms =[
    {'id':1, 'name':'let learn python'},
    {'id':2, 'name':'Design the world'},
    {'id':3, 'name':'make the world better'}
]

def home(request):
    brands = Brand.objects.all()
    categories = Category.objects.all().order_by('-created')[:6]
    context ={'rooms':rooms, 'brands':brands, 'categories':categories, 'testid':123}
    return render(request, 'base/home.html', context)



def room(request,pk):
    room = None
    for i in rooms: 
        if i['id'] == int(pk):
            room = i
    context ={'room':room}
    return render(request, 'base/room.html',context)

def brand_categories(request):
    #brand = Brand.objects.get(id=pk)
    #brand_cat = brand.category_set.all()
    #brand = Brand.objects.all()
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
        print(category_id)
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
