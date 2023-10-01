
from django.urls import path, include
from .views import home, list_properties, property_view

urlpatterns = [
    path('', home),
    path('list_properties/', list_properties),
    path('property_view/<int:prop_id>', property_view),
]
