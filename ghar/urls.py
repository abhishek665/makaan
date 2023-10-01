
from django.urls import path, include
from .views import home, list_properties, property_view, test_html

urlpatterns = [
    path('', home),
    path('list_properties/', list_properties),
    path('test_html/', test_html),
    path('property_view/<int:prop_id>', property_view),
]
