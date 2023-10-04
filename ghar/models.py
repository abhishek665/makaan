from django.db import models
from django.contrib.auth.models import User

from multiupload.fields import MultiFileField


# Create your models here.


class Agent(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name


class Property(models.Model):
    ref = models.ForeignKey(Agent, on_delete=models.CASCADE)
    property_id = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    area = models.PositiveBigIntegerField(blank=True, null=True)
    bhk = models.CharField(max_length=255, blank=True, null=True)
    price = models.PositiveBigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(default=0)
    ownership = models.CharField(max_length=255)  # first hand, second hand
    boundary = models.BooleanField(default=False)
    gated = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    how_soon = models.CharField(max_length=255, blank=True, null=True)  # ready to move or waiting
    owner_count = models.IntegerField(default=1)  # how many registries are there for the property
    owner_name = models.CharField(max_length=255, blank=True, null=False)
    owner_contact = models.CharField(max_length=255, null=True, blank=True)
    floor = models.DecimalField(default=0.0, max_digits=10, decimal_places=1)
    nearest_places = models.CharField(max_length=255, blank=True, null=True)

    desc = models.TextField(blank=True, null=False)
    property_title = models.CharField(max_length=100, blank=True, null=True)
    furnishing = models.CharField(max_length=50, blank=True, null=True)
    posted_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.owner_name + ' - ' + str(self.property_id)


def property_image_path(instance, filename):
    return f'property/{instance.ref.property_id}/{instance.ref.type}/{instance.ref.place}/{filename.replace(" ", "")}'


class PropertyImage(models.Model):
    ref = models.ForeignKey(Property, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image2 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image3 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image4 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image5 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image6 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image7 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image8 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image9 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image10 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image11 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image12 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image13 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image14 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image15 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image16 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image17 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image18 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image19 = models.ImageField(upload_to=property_image_path, blank=True, null=True)
    image20 = models.ImageField(upload_to=property_image_path, blank=True, null=True)

    def __str__(self):
        return str(self.ref)


class CustomerContact(models.Model):
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name + ' - ' + str(self.number)


class CustomerQueries(models.Model):
    customer = models.ForeignKey(CustomerContact, on_delete=models.CASCADE)
    query = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.customer.name + ' - ' + str(self.customer.number)