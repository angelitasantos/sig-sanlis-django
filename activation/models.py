from django.db import models
from typing import Optional
from django.contrib.auth.models import User

class Company(models.Model):
    token_company = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=250)

    start_data = models.DateTimeField()
    cnpj = models.CharField(max_length=20, blank=True)
    insc_est = models.CharField(max_length=20, blank=True)
    insc_mun = models.CharField(max_length=20, blank=True)

    street = models.CharField(max_length=100, blank=True)
    number = models.IntegerField(blank=True)
    complement = models.CharField(max_length=20, blank=True)
    district = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zipcode = models.CharField(max_length=15, blank=True)
    google_maps_link = models.TextField(blank=True)

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=25, blank=True)
    whatsapp_number = models.CharField(max_length=25, blank=True)
    whatsapp_link = models.CharField(max_length=250, blank=True)

    site_link = models.CharField(max_length=250, blank=True)
    instagram_link = models.CharField(max_length=250, blank=True)
    linkedin_link = models.CharField(max_length=250, blank=True)
    facebook_link = models.CharField(max_length=250, blank=True)

    user_company = models.ForeignKey(User, blank=True, on_delete=models.DO_NOTHING)

def __str__(self):
    return self.name