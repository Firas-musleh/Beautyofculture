from . import views
from django.urls import re_path
from django.urls import path
from django.conf.urls import url


app_name = 'ost'

urlpatterns = [
    path('search', views.search, name="search"),
    path('', views.all_prodcut, name='product_list'),
    path('<slug:slug>', views.one_prodcut, name='one_prodcut'),
    path('about_us/', views.about_us, name='about_us'),
    # url(r'^(?P<category_name>[-\w]+)/$',
    #     views.all_prodcut, name='product_list'),
   
    path('<slug:category_slug>/', views.all_prodcut,
         name="product_list_by_category"),

]
