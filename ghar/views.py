import json
import time

from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from .models import PropertyImage, Property, CustomerQueries, CustomerContact, Agent
from itertools import chain
from .utils import img_filter_condition
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
            data = Property.objects.filter(address__icontains=place.lower(), type='plots', area__lte=int(area),
                                           price__lte=int(price))
            images = PropertyImage.objects.filter(ref__in=[x for x in data])
            return render(request, 'list-property.html', {'data': zip(data, images)})
        elif inc_data['what'].lower() == 'houses':
            area = inc_data['area']
            data = Property.objects.filter(address__icontains=place.lower(), type='houses', area__lte=int(area),
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


@login_required(login_url='/signin')
def prop_img_upload(request):
    if request.POST:
        data = request.POST
        images = request.FILES.getlist('images[]')
        print(request.POST, len(request.FILES.getlist('images[]')))
        my_data = {}
        my_img = {}
        img_key = 'image'
        for i in data.keys():
            my_data[i] = data[i]
        my_data.pop('csrfmiddlewaretoken')
        my_data.pop('agent')
        for i in my_data.keys():
            print(i, my_data[i], my_data[i] == 'on')
            if my_data[i] == 'on':
                my_data[i] = True
            if my_data[i] == 'off':
                my_data[i] = False
        print(my_data)
        agent = Agent.objects.get(username=request.user)
        print('ageeeeeeeeeeeeeeeeeeee', agent)
        property = Property(ref=agent, **my_data)
        property.save()
        for i in range(0, len(images)):
            my_img[img_key + str(i+1)] = images[i]

        print(my_img)
        PropertyImage(ref=property, **my_img).save()

        return render(request, 'prop-img-upload.html', {'status': True, 'msg': 'Property saved successfully.'})

    return render(request, 'prop-img-upload.html')


def sign_in(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)
        print(user)
        if user:
            print(user)
            login(request, user)
            return redirect('/prop_img_upload')
    return render(request, 'login.html')


def sign_out(request):
    pass


def sign_up(request):
    pass