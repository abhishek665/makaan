from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Agent)
admin.site.register(PropertyImage)
admin.site.register(Property)
admin.site.register(CustomerContact)
admin.site.register(CustomerQueries)

# from .forms import handler, prop_img_upload
# from django.contrib import admin
# from .models import PropertyImage


# @admin.register(PropertyImage)
# class MyModelAdmin(admin.ModelAdmin):
#     form = prop_img_upload.MyModelForm