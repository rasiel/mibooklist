from django.db import models
from django.contrib.auth.models import User

ACCOUNT_STATUS = (
    ('AC', 'Active'),
    ('SD', 'Suspended'),
    ('PP', 'Pending Payment'),
    ('PV', 'Pending Validation')
)
PAYMENT_OPTIONS = (
    ('GC', 'Google Checkout'),
    ('LB', 'Local Bank Deposit')
)
DISTRICT_CHOICES = (
    ('CZ', 'Corozal'),
    ('OW', 'Orange Walk'),
    ('BZ', 'Belize'),
    ('CY', 'Cayo'),
    ('SC', 'Dangriga'),
    ('TO', 'Toledo')
)
# Create your models here.
class Seller (models.Model):
    user = models.ForeignKey(User,related_name="seller_user")
    screen_name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=2, choices=DISTRICT_CHOICES, blank=True, null=True)
    home_number = models.CharField(max_length=25, blank=True, null=True)
    hide_phone = models.BooleanField(blank=True)
    cellular_number = models.CharField(max_length=25, blank=True, null=True)
    hide_cellular = models.BooleanField(blank=True)
    hide_email = models.BooleanField(blank=True)
    signup_date = models.DateField(auto_now_add=True)
    account_status = models.CharField(max_length=2,choices=ACCOUNT_STATUS, default='PV')
    payment_option = models.CharField(max_length=2,choices=PAYMENT_OPTIONS, default='GC', blank=True, null=True)
    
    class Meta:
        get_latest_by = '-signup_date'
        ordering = ['screen_name']

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return "/sellers/%s/" % (self.user.username)  