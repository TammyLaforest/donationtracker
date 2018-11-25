from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from shortuuidfield import ShortUUIDField

from django.core.validators import validate_email


class Contact(models.Model):

    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    uuid = ShortUUIDField(unique=True, primary_key = True,)
    created_on = models.DateField(auto_now_add=True)

    BOOKTYPE_CHOICES = (
    ('Donor', (
            ('member', 'Member'),
            ('regular', 'Regular'),
            ('first_time', 'First_Time'),
            ('annual', 'Annual'),
            ('grant', 'Grant'),
            ('otherdonor', 'Otherdonor'),
        )
    ),
    ('Vendor', (
            ('biller', 'Biller'),
            ('contractor', 'Contractor'),
            ('seller', 'Seller'),
        )
    ),
    ('unknown', 'Unknown'),
    ('other', 'Other'),

    )

    booktype = models.CharField(
        max_length=20,
        choices=BOOKTYPE_CHOICES,
        default='Unknown',
    )
    CONTACTTYPE_CHOICES = (
        ('company', 'Company'),
        ('individual', 'Individual'),
        ('couple', 'Couple'),
        ('other', 'Other'),
    )

    contacttype = models.CharField(
        max_length=20,
        choices=CONTACTTYPE_CHOICES,
        default='Other',
    )

    company = models.CharField(max_length=50,blank=True )
    first_name1 = models.CharField(max_length=30, blank=True )
    last_name1 = models.CharField(max_length=30, blank=True )
    first_name2 = models.CharField(max_length=30, blank=True )
    last_name2 = models.CharField(max_length=30, blank=True )
    address_number = models.CharField(max_length=20, blank=True )
    address_street = models.CharField(max_length=30, blank=True )
    address_street2 = models.CharField(max_length=30, blank=True )
    address_city = models.CharField(max_length=30, blank=True )
    address_state = models.CharField(max_length=30, blank=True )
    address_postalcode = models.CharField(max_length=30, blank=True )
    address_country = models.CharField(max_length=30, default='USA', blank=True )
    phone1 = models.CharField(max_length=20, blank=True )
    phone2 = models.CharField(max_length=20, blank=True )
    email1 = models.EmailField(validators=[validate_email], blank=True )
    email2 = models.EmailField(validators=[validate_email], blank=True )
    note = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'contacts'

    # def clean(self):
    #     if not (self.company or
    #         self.first_name1 or
    #         self.last_name1 or
    #         self.last_name2 or
    #         self.first_name2):
    #         raise ValidationError("You must specify a contact name")

    @property
    def full_name(self):
        return u'%s %s' % (self.first_name1, self.last_name1)

    def __unicode__(self):
        return u'%s' % self.full_name


    @property
    def couple(self):
        return u'%s %s & %s %s' % (self.first_name1, self.last_name1,
            self.first_name2, self.last_name2,)

    def __unicode__(self):
        return u'%s' % self.couple  

    def __unicode__(self):
        return u'%s' % self.company


    # @models.permalink
    # def get_absolute_url(self):
    #     return 'contact_detail', [self.uuid]
    #
    # @models.permalink
    # def get_update_url(self):
    #     return 'contact_update', [self.uuid]
    #
    # @models.permalink
    # def get_delete_url(self):
    #     return 'contact_delete', [self.id]