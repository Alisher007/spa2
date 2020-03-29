from django import forms

from reservations.models import Res
from customers.models import Customer

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Res

        fields = [
            'customerid',
            'products',
            'roomid',
            'arrdate',
            'starttime',
            'endtime',
        ]
        
class TestForm(forms.ModelForm):
    class Meta:
        model = Res

        fields = [
            'customerid',
            'products',
            'roomid',
            'arrdate',
            'starttime',
            'endtime',
        ]

    def __init__(self, *args, **kwargs):
        products = kwargs.get('products', None)
        if products:
            kwargs.update(initial={
                # 'field': 'value'
                'products': products.split(',')
            })
        print(products, ' init')
        super(TestForm, self).__init__(*args, **kwargs)
