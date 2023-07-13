
from django.urls import path, include
from .views import home, list_properties

urlpatterns = [
    path('', home),
    path('list_properties/', list_properties),
]
