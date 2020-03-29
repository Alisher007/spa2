from django.urls import path, include
from reservations import views

app_name= 'res'
urlpatterns = [
    path('', views.res_list, name='list'),
    path('list/<slug:slug>/', views.res_list, name='list'),
    path('ajax/', views.res_ajax, name='ajax'),
    path('search/', views.customer_search, name='search'),
    path('product-search/', views.product_search, name='product-search'),
    path('create/', views.res_create, name='create'),
    path('delete/<int:id>/', views.res_delete, name='delete'),
    path('update/<int:id>/', views.res_update, name='update'),
]