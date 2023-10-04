
from django.urls import path, include
from .views import home, list_properties, property_view, test_html, customer_contact

from .forms import handler

urlpatterns = [
    path('', home),
    path('list_properties/', list_properties),
    path('test_html/', test_html),
    path('property_view/<int:prop_id>', property_view),
    path('customer_contact/', customer_contact),
    # path('prop_img_upload/', handler.upload_images),
]
