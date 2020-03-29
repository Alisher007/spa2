from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerForm
from .models import Customer
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.
def customer_list(request,):

    customers = Customer.objects.all()

    context = {
        'customers': customers,
    }
    return render(request, 'customers/list.html', context)

def customer_edit(request,id):
    customer_target = get_object_or_404(Customer, pk=id)
    form = CustomerForm(request.POST or None , instance=customer_target)
    if form.is_valid():
        form.save()
        if request.is_ajax:
            return JsonResponse({'data':'ok'})
        messages.info(request,' customer has been updated')
        return redirect('customers:list')
    context = {
        'form': form,
    }
    return render(request, 'customers/detail.html', context)

def customer_add(request):
    
    email = request.POST['email']
    name = request.POST['name']
    customer = Customer(email = request.POST['email'], name = request.POST['name'])
    if len(name) == 0 or len(email) == 0:
        messages.error(request,' name and email should not be empty')
    else:
        messages.info(request,' customer has been created')
        customer.save()
    return redirect('customers:list')

def customer_delete(request, id):
    customer = Customer.objects.get(id=id)
    messages.info(request,f'{customer} has been deleted')
    customer.delete()
    return redirect('customers:list')