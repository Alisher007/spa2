from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Q

from datetime import date
from products.models import Product
from customers.models import Customer
from products.models import Product
from reservations.forms import ReservationForm, TestForm
from reservations.models import Res, Timelist, Room
import json
from django.http import HttpResponseRedirect
from django.contrib import messages


def home(request):
    return render(request, 'reservation/home.html')

def res_update(request,id):
    res_target = get_object_or_404(Res, pk=id)
    form = ReservationForm(request.POST or None , instance=res_target)
    if form.is_valid():
        res_time_in = list(range(int(request.POST.get('starttime')), int(request.POST.get('endtime')) + 1 ))
        res_duplicate = Res.objects.filter(
            Q(arrdate=request.POST.get('arrdate')),
            Q(roomid=request.POST.get('roomid')),
            Q(starttime__in=(res_time_in)) |
            Q(endtime__in=(res_time_in))
        ).exclude(pk=id).count()
        if res_duplicate >= 1:
            messages.error(request, 'There is already reservation exists')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.info(request,' reservation has been updated')
            form.save()
        return redirect('res:list', slug=res_target.arrdate)
    tester = ''
    for target_list in res_target.products.values_list('id', flat=True):
        tester += str(target_list) + ','
    context = {
        'form': form,
        'res_id': id,
        'customer': res_target.customerid.name,
        'customerid': res_target.customerid.id,
        'products': ','.join(list(res_target.products.values_list('name', flat=True))),
        'productsid': tester,
    }
    return render(request, 'reservation/res_update.html', context)

def res_create_test(request,):
    form = TestForm(request.POST)
    if form.is_valid():
        if int(request.POST.get('starttime')) >= int(request.POST.get('endtime')):
            messages.error(request, 'start time should before the end time')
        instance = form.save(commit=False)
        instance.user = request.user
        res_time_in = list(range(int(request.POST.get('starttime')), int(request.POST.get('endtime')) + 1 ))
        res_duplicate = Res.objects.filter(
            Q(arrdate=request.POST.get('arrdate')),
            Q(roomid=request.POST.get('roomid')),
            Q(starttime__in=(res_time_in)) |
            Q(endtime__in=(res_time_in))
        ).count()
        if res_duplicate >= 1:
            messages.error(request, 'There is already reservation exists')
            return HttpResponseRedirect(request.path_info)
        else:
            instance.save()
        context = {
            'form': form,
        }
        return redirect('res:list', slug=request.POST.get('arrdate') )
    context = {
        'form': form,
    }
    return render(request, 'reservation/res_test.html', context)

def res_create(request,):
    initial_data = {}
    initial_data['starttime'] = request.GET.get('time')
    initial_data['roomid'] = request.GET.get('table')
    initial_data['arrdate'] = request.GET.get('date')
    form = ReservationForm(request.POST or None, initial = initial_data)
    if form.is_valid():
        if int(request.POST.get('starttime')) >= int(request.POST.get('endtime')):
            messages.error(request,' the end time should be higher than the start time')
            return HttpResponseRedirect(request.path_info)
        instance = form.save(commit=False)
        print(request.user, ' request.user')
        instance.user = request.user
        res_time_in = list(range(int(request.POST.get('starttime')), int(request.POST.get('endtime')) + 1 ))
        res_duplicate = Res.objects.filter(
            Q(arrdate=request.POST.get('arrdate')),
            Q(roomid=request.POST.get('roomid')),
            Q(starttime__in=(res_time_in)) |
            Q(endtime__in=(res_time_in))
        ).count()
        if res_duplicate >= 1:
            messages.error(request,' the room is occupied')
        else:
            messages.info(request,' reservation has been created')
            instance.save()
            form.save_m2m()
        context = {
            'form': form,
        }
        return redirect('res:list', slug=request.POST.get('arrdate') )
    context = {
        'form': form,
    }
    return render(request, 'reservation/res_create.html', context)

def res_delete(request, id):
    print(request.POST.get('date'))
    res = Res.objects.get(id=id)
    messages.info(request,f'{res} has been deleted')
    res.delete()
    return JsonResponse({'data':'ok'}, safe=False)

def res_list(request,slug=None):
    today_ = str(date.today())
    if slug == None:
        slug = today_
    # getting the reservations for selected date
    res = list(Res.objects.filter(arrdate=slug).prefetch_related('products'))
    table = list(Room.objects.all())
    time_list = list(Timelist.objects.all())
    # creating availibility table
    avail_list = [[{
        'table':str(ta),'table_id':ta.id,'time':str(ti),'time_id':ti.id, 'status':'vacant', 'date':slug
        } for ta in table] for ti in time_list]

    # inserting queryset data into availability table
    product_list = []
    product_list_id = []
    if res:
        for avail_list1 in avail_list:
            for avail_list2 in avail_list1:
                for re in res:
                    if re.roomid.pk == avail_list2.get('table_id') and re.starttime.pk <= avail_list2.get('time_id') and re.endtime.pk >= avail_list2.get('time_id'):
                        avail_list2.update({
                        'table':avail_list2.get('table'),
                        'time':avail_list2.get('time'), 
                        'customer': re.customerid.name,
                        'res_id':re.pk,
                        'products': ','.join(re.products.values_list('name', flat=True)),
                        'products_id': ','.join(str(re.products.values_list('id', flat=True))),
                        'status':'' ,
                        'occupied':'occupied'})
                        product_list = []
                        product_list_id = []
    context = {
        'avail': avail_list,
        'table': table,
        'time_list': time_list,
        'date': today_,
        }
    return render(request, 'reservation/res_list.html', context)

def res_ajax(request,):
    room_json = list(Room.objects.values())
    time_list_json = list(Timelist.objects.values())
    context = {
        'room': room_json,
        'time': time_list_json,
        }
    return JsonResponse(context, safe=False)

def customer_search(request):
    ctx = {}
    url_parameter = request.GET.get("q")
    if url_parameter:
        customers = Customer.objects.filter(name__icontains=url_parameter)
    else:
        customers = Customer.objects.all()[:5]
    
    ctx["customers"] = customers
    data_dict = {"html_customers-search": 'test'}
    if request.is_ajax():
        
        html = render_to_string(
            template_name="reservation/customers-search.html", context={"customers": customers}
        )
        data_dict = {"html_customers-search": html}

    return JsonResponse(data=data_dict, safe=False)

def product_search(request):
    ctx = {}
    url_parameter = request.GET.get("q")
    if url_parameter:
        products = Product.objects.filter(name__icontains=url_parameter)
    else:
        products = Product.objects.all()[:5]
    
    ctx["products"] = products
    data_dict = {"html_products-search": 'test'}
    if request.is_ajax():
        
        html = render_to_string(
            template_name="reservation/products-search.html", context={"products": products}
        )
        data_dict = {"html_products-search": html}

    return JsonResponse(data=data_dict, safe=False)
