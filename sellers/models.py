from django.db import models
from django.contrib.auth.models import User

ACCOUNT_STATUS = (
    ('AC', 'Active'),
    ('SD', 'Suspended'),
    ('PP', 'Pending Payment'),
    ('PV', 'Pending Validation')
)
SUPPORT_STATUS = (
    ('NW', 'New'),
    ('RD', 'Read'),
    ('OP', 'Open'),
    ('CL', 'Closed')
)
PAYMENT_OPTIONS = (
    ('GC', 'Google Checkout'),
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

    def __unicode__(self):
        return self.user.username
    
    def get_full_name(self):
        return "%s %s" %(self.user.first_name, self.user.last_name)

    def get_absolute_url(self):
        return "/sellers/%s/" % (self.user.username)  
    
class SupportMessage(models.Model):
    seller = models.ForeignKey(Seller,related_name="support_message_seller")
    message = models.TextField()
    status = models.CharField(max_length=2, choices=SUPPORT_STATUS, default='NW')
    date_received = models.DateTimeField(auto_now_add=True, editable=False)
    
    class Meta:
        get_latest_by = '-date_received'
        ordering = ['-date_received', 'status']
    
    def __unicode__(self):
        return "%s - id: %s" %(self.seller, self.id)
    
    def get_absolute_url(self):
        return "/support-message/%s/" % (self.id)  