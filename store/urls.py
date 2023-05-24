from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<slug:category_address>/<slug:address>',
         views.product_detail, name='product_detail'),
    path('<slug:category_address>/',
         views.category_list, name='category_list'),

]
