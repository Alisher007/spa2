from django.urls import path
from customers import views

app_name= 'customers'
urlpatterns = [
    path('', views.customer_list, name='list'),
    path('add/', views.customer_add, name='add'),
    path('delete/<int:id>/', views.customer_delete, name='delete'),
    path('edit/<int:id>/', views.customer_edit, name='edit'),
]