from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('room/<str:pk>', views.room, name ="room"),
    path('pages/pages/categories/', views.brand_categories, name ="brand_categories"),
    path('pages/components/post-list.html/', views.Category_items, name ="category_items"),

]
