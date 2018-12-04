from django.db import models
from django import forms

from django.urls import reverse

from shortuuidfield import ShortUUIDField

from django.core.validators import validate_email
from django.forms import ModelForm

from django.contrib.auth.models import User


# Generic contact model
class Contact(models.Model):
    Owner = models.ForeignKey(User, on_delete = models.CASCADE)
    uuid = ShortUUIDField(unique=True, primary_key = True,)
    Created_On = models.DateField(auto_now_add=True)
    CATEGORY_CHOICES = ( ('donor', 'Donor'), ('vendor', 'Vendor'))

    Contact_Category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Donor',
    )

    Account = models.CharField(max_length=100, blank=True)

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

    def to_class_name(value):
        return value.__class__.__name__


    # def get_absolute_url(self):
    #     return u'/some_url/%d' % self.id

#
# class Format(models.Model):
#     FORMAT_CHOICES = (
#         ('business', 'Business'),
#         ('individual','Individual'),
#         ('couple', 'Couple'),
#         ('other', 'Other'),
#     )
#     Format = models.CharField(
#         max_length=20,
#         choices=FORMAT_CHOICES,
#         default='Other',
#     )
#
# # Base contact model. All fields in all forms
# class Contact_old(models.Model):
#     Owner = models.ForeignKey(User, on_delete = models.CASCADE)
#     uuid = ShortUUIDField(unique=True, primary_key = True,)
#     Created_On = models.DateField(auto_now_add=True)
#     Note = models.TextField(blank=True)
#     Account = models.CharField(max_length=50)
#
#     Title = models.CharField(max_length=10, blank=True )
#     First_Name = models.CharField(max_length=30, blank=True )
#     Last_Name = models.CharField(max_length=30, blank=True )
#     Phone = models.CharField(max_length=20, blank=True )
#     Email = models.EmailField(validators=[validate_email], blank=True )
#
#     address = models.CharField(max_length=255, blank=True)
#     city = models.CharField(max_length=255,blank=True)
#     state = models.CharField(max_length=2,blank=True)
#     postal_code = models.CharField(max_length=20,blank=True)
#     country = models.CharField(max_length=30, default='USA', blank=True )
#
#
# class Individual(models.Model):
#         Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
#         Format = 'individual'
#         SUBCATEGORY_CHOICES =(
#                 ('member', 'Member'),
#                 ('regular', 'Regular'),
#                 ('first_time', 'First_Time'),
#                 ('annual', 'Annual'),
#                 ('otherdonor', 'Otherdonor'),
#                 )
#         Subcategory = models.CharField(
#             max_length=20,
#             choices=SUBCATEGORY_CHOICES,
#             default='Otherdonor',
#             )
#         Account = models.CharField(max_length=50)
#         def __str__(self):
#             if Last_Name is None:
#                 Account = Contact.objects.get(pk=uuid)
#             else:
#                 Account = [Last_Name + ", " + First_Name]
#             return Account
#
#         @property
#         def full_name(self):
#             return u'%s %s' % (self.First_Name1, self.Last_Name1)
#
#         def __unicode__(self):
#             return u'%s' % self.full_name
#
# # For formset with multiple individuals
# class Spouse(models.Model):
#     Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
#     Format = 'couple'
#     SUBCATEGORY_CHOICES =(
#             ('member', 'Member'),
#             ('regular', 'Regular'),
#             ('first_time', 'First_Time'),
#             ('annual', 'Annual'),
#             ('otherdonor', 'Otherdonor'),
#             )
#     Subcategory = models.CharField(
#         max_length=20,
#         choices=SUBCATEGORY_CHOICES,
#         default='Otherdonor',
#         )
#     Title2 = models.CharField(max_length=10, blank=True )
#     First_Name2 = models.CharField(max_length=30, blank=True )
#     Last_Name2 = models.CharField(max_length=30, blank=True )
#     Email2 = models.EmailField(validators=[validate_email], blank=True )
#     Phone2 = models.CharField(max_length=20, blank=True )
#     Account = models.CharField(max_length=50)
#     def __str__(self):
#         if Last_Name is None:
#             Account = Contact.objects.get(pk=uuid)
#         elif Last_Name2 is None:
#             Account = (Last_Name + ", " + First_Name)
#         elif Last_Name == Last_Name2:
#             Account = [Last_Name + ", " + First_Name + " & " + First_Name2]
#         else:
#             Account = [Last_Name + ", " + First_Name + " & " + Last_Name2 + ", " + First_Name2]
#         return Account
#     @property
#     def couple(self):
#         return u'%s %s & %s %s' % (self.First_Name1, self.Last_Name1,
#             self.First_Name2, self.Last_Name2,)
#
#     def __unicode__(self):
#         return u'%s' % self.couple
#
# class Company_Donor(models.Model):
#     Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
#     Format = 'business'
#     SUBCATEGORY_CHOICES =(
#             ('regular', 'Regular'),
#             ('first_time', 'First_Time'),
#             ('annual', 'Annual'),
#             ('grant', 'Grant'),
#             ('otherdonor', 'Otherdonor'),
#             )
#     Subcategory = models.CharField(
#         max_length=20,
#         choices=SUBCATEGORY_CHOICES,
#         default='Otherdonor',
#         )
#     Company_Name = models.CharField(max_length=50)
#     Account = models.CharField(max_length=50, default = Company_Name)
#
# class Company_Vendor(models.Model):
#     Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
#     Format = 'business'
#     SUBCATEGORY_CHOICES =(
#             ('biller', 'Biller'),
#             ('contractor', 'Contractor'),
#             ('seller', 'Seller'),
#             ('othervendor', 'Othervendor'),
#             )
#     Subcategory = models.CharField(
#         max_length=20,
#         choices=SUBCATEGORY_CHOICES,
#         default='OtherDonor',
#         )
#     Company_Name = models.CharField(max_length=50,blank=True )
#     Account = models.CharField(max_length=50, default = User.username)
#
#
# class Other(models.Model):
#     Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
#     Format = 'other'
#     Subcategory = 'other'
#     Company_Name = models.CharField(max_length=50)
#     Title2 = models.CharField(max_length=10, blank=True )
#     First_Name2 = models.CharField(max_length=30, blank=True )
#     Last_Name2 = models.CharField(max_length=30, blank=True )
#     Account = models.CharField(max_length=50)
#     def __str__(self):
#         if Company_Name:
#             Account = Company_Name
#         elif Last_Name:
#             Account = Last_Name
#         else:
#             Account = Contact
#         return Account
#
#
# # Categories models
# class Category(models.Model):
#     CATEGORY_CHOICES = (('Donor', 'donor'),('Vendor', 'vendor'), ('Other', 'other'))
#     Category = models.CharField(
#         max_length=20,
#         choices=CATEGORY_CHOICES,
#         default='Other',
#     )
#
class donor_categories(models.Model):
    Category = 'donor'
    CATEGORY_CHOICES = (
    ('member', 'Member'),
    ('regular', 'Regular'),
    ('first_time', 'First_Time'),
    ('annual', 'Annual'),
    ('grant', 'Grant'),
    ('otherdonor', 'Otherdonor')
    )
    Category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='otherdonor',
    )
    def get_absolute_url(self):
        return u'/some_url/%d' % self.id

class vendor_categories(models.Model):
    Category = 'vendor'
    SUBCATEGORY_CHOICES =(
            ('biller', 'Biller'),
            ('contractor', 'Contractor'),
            ('seller', 'Seller'),
            ('othervendor', 'Othervendor')
            )
    Subcategory = models.CharField(
        max_length=20,
        choices=SUBCATEGORY_CHOICES,
        default='othervendor',
        )
    # def get_absolute_url(self):
    #     return u'/some_url/%d' % self.id

class other_categories(models.Model):
    Category = 'other'
    Subcategory = 'other'

    # def get_absolute_url(self):
    #     return u'/some_url/%d' % self.id



# # Allows for multiple addresses
# class Address(models.Model):
#     Contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
#     address_type = models.CharField(max_length=10,blank=True)
#     address = models.CharField(max_length=255, blank=True)
#     city = models.CharField(max_length=255,blank=True)
#     state = models.CharField(max_length=2,blank=True)
#     postal_code = models.CharField(max_length=20,blank=True)
#     country = models.CharField(max_length=30, default='USA', blank=True )
