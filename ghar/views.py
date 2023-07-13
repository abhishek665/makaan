import time

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'body.html')


def list_properties(request):
    print(request.POST)
    return render(request, 'list-property.html')