from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('pages/pages/home.html',views.home, name="home-js"),
    path('room/<str:pk>', views.room, name ="room"),
    path('pages/pages/categories/', views.brand_categories, name ="brand_categories"),
    path('pages/components/post-list.html/', views.Category_items, name ="category_items"),
    path('pages/pages/offer.html/', views.offer, name ="offer"),
    path('pages/pages/item.html/', views.item, name ="item"),
    path('pages/pages/categories-list.html',views.categories, name="categories"),

]
