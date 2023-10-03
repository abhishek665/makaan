from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Agent(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.username.username


class Property(models.Model):
    ref = models.ForeignKey(Agent, on_delete=models.CASCADE)
    property_id = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    bhk = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(default=0)
    ownership = models.CharField(max_length=255)  # first hand, second hand
    boundary = models.IntegerField(default=0)
    gated = models.IntegerField(default=0)
    is_active = models.IntegerField(default=0)
    how_soon = models.CharField(max_length=255, blank=True, null=True)  # ready to move or waiting
    owner_count = models.IntegerField(default=1)  # how many registries are there for the property
    floor = models.IntegerField(default=0)


def property_image_path(instance, filename):
    return f'/media/property/{instance.ref.property_id}/{instance.ref.type}/{instance.ref.place}/{filename}'


class PropertyImage(models.Model):
    ref = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=property_image_path)