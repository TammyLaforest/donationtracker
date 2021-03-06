from django.db import models
from django.conf import settings
from django.urls import reverse
from shortuuidfield import ShortUUIDField
from django.core.validators import validate_email

from django.forms import forms
from django.contrib.auth import get_user_model
User = get_user_model()

# Generic contact model
class Contact(models.Model):

    Owner = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="Owner", null=True, blank=True)
    uuid = ShortUUIDField(unique=True, primary_key = True,)
    Account= models.CharField(max_length=120, blank=False)
    Created_On = models.DateField(auto_now_add=True)
    CATEGORY_CHOICES = ( ('donor', 'Donor'), ('vendor', 'Vendor'))

    Contact_Category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Donor',
    )

    Address = models.CharField(max_length=255, blank=True)
    City = models.CharField(max_length=255,blank=True)
    State = models.CharField(max_length=2,blank=True)
    Postal_code = models.CharField(max_length=20,blank=True)
    Country = models.CharField(max_length=30, default='USA', blank=True )

    Company = models.CharField(max_length=50,blank=True )

    First_Name = models.CharField(max_length=30, blank=True )
    Last_Name = models.CharField(max_length=30, blank=True )
    Email = models.EmailField(validators=[validate_email], blank=True )
    Phone = models.CharField(max_length=20, blank=True )

    First_Name2 = models.CharField(max_length=30, blank=True )
    Last_Name2 = models.CharField(max_length=30, blank=True )
    Phone2 = models.CharField(max_length=20, blank=True )
    Email2 = models.EmailField(validators=[validate_email], blank=True )
    Note = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Contacts'
        unique_together = (("Last_Name", "First_Name"),)
        unique_together = (("Last_Name2", "First_Name2"),)
        unique_together = (("Company", "Owner"),)
        ordering = ['Company','Last_Name', 'First_Name',  ]

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.uuid})
        # return "contact-detail/%s/" %self.uuid

class Format(models.Model):
    FORMAT_CHOICES = (
        ('business', 'Business'),
        ('individual','Individual'),
        ('couple', 'Couple'),
        ('other', 'Other'),
    )
    Format = models.CharField(
        max_length=20,
        choices=FORMAT_CHOICES,
        default='Other',
    )
