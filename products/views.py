from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.shortcuts import reverse, redirect


from .models import Product
from .forms import ProductForm

class ProductListView(ListView):

    model = Product

class ProductDetailView(DetailView):

    model = Product

class ProductCreateView2(CreateView):
    model = Product
    fields = ['name']


class ProductDeleteView(DeleteView):
    model = Product

    def get_success_url(self):
            return reverse('products:product-create')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name']
    template_name = 'products/product_update.html'

class ProductCreateView(CreateView):
    form_class = ProductForm
    # success_url = 'products:product-create'
    template_name = 'products/product_list.html'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Product.objects.all()
        return super(ProductCreateView, self).get_context_data(**kwargs)
    
    def get_success_url(self):
            return reverse('products:product-create')