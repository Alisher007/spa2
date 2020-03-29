from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'products'
urlpatterns = [
    path('', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete')
]