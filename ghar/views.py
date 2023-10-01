import time

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def test_html(request):
    return render(request, 'test-html.html')


def home(request):
    return render(request, 'body.html')


def list_properties(request):
    print(request.POST)
    return render(request, 'list-property.html')


def property_view(request, prop_id):
    return render(request, 'prop-view.html')