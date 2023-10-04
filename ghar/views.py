import json
import time

from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import PropertyImage, Property, CustomerQueries, CustomerContact
from itertools import chain
from .utils import img_filter_condition


# Create your views here.

def test_html(request):
    return render(request, 'test-html.html')


def home(request):
    return render(request, 'body.html')


def list_properties(request):
    inc_data = ''
    try:
        inc_data = json.loads(request.POST['data'])
    except Exception as e:
        print(e)
    print(inc_data['place'], inc_data['what'], inc_data)
    print(int(inc_data['price']) < 3000000)
    if inc_data:
        data = ''
        place = inc_data['place']
        price = inc_data['price']
        if inc_data['what'].lower() == 'plots':
            area = inc_data['area']
            data = Property.objects.filter(address__contains=place, type='plots', area__lte=int(area),
                                           price__lte=int(price))
            images = PropertyImage.objects.filter(ref__in=[x for x in data])
            return render(request, 'list-property.html', {'data': zip(data, images)})
        elif inc_data['what'].lower() == 'houses':
            area = inc_data['area']
            data = Property.objects.filter(address__contains=place, type='houses', area__lte=int(area),
                                           price__lte=int(price))
            images = PropertyImage.objects.filter(ref__in=[x for x in data])
            print(images, data, zip(data, images))
            print(data)
            return render(request, 'list-property.html', {'data': zip(data, images)})
    return render(request, 'list-property.html')


def property_view(request, prop_id):
    try:
        print(prop_id)
        data = Property.objects.filter(id=int(prop_id))
        images = list(PropertyImage.objects.filter(ref__in=[x for x in data]).values())
        a = images[0]
        new_image_data = []
        print(a)
        for i in a.keys():
            if a[i] != '':
                new_image_data += [a[i]]
        comb_data = zip(data, images)
        new_image_data = new_image_data[3:]
        print(new_image_data)
        return render(request, 'prop-view.html', {'data': comb_data, 'images': new_image_data})
    except Exception as e:
        print(e)
        return render(request, 'prop-view.html')
    # return render(request, 'prop-view.html')


def customer_contact(request):
    if request.POST:
        try:
            print('name', request.POST.get('name'), request.POST)
            name = request.POST.get('name')
            number = request.POST.get('number')
            filters = json.loads(request.POST.get('filters'))
            print('filters', filters)

            if len(number) != 10:
                print('11111111111')
                return HttpResponse(json.dumps({'status': False, 'msg': 'Please enter a valid 10 digit number.'}))
            if not number.isdigit():
                print('22222222222222')
                return HttpResponse(json.dumps({'status': False, 'msg': 'Please enter a valid 10 digit number. It should contain only numbers.'}))
            print('processed')
            cc = CustomerContact(name=name, number=number)
            cc.save()
            CustomerQueries(customer=cc, query=filters).save()

            return HttpResponse(json.dumps({'customer_contact': number, 'status': True}))
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({'status': False, 'msg': str(e)}))
    return HttpResponse(json.dumps({'status': False, 'msg': 'Invalid Request'}))