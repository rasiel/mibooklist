from mibooklist.sellers.models import *
from django.contrib import admin

class SellerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'home_number',
                           'hide_phone', 'cellular_number',
                           'hide_cellular', 'account_status', 
                           'hide_email', 'location']})
    ]
    list_display = ('user', 'get_full_name', 'account_status', 'signup_date')
    list_filter = ('account_status',)
    
admin.site.register(Seller, SellerAdmin)

class SupportMessageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['seller', 'message', 'status']})
    ]
    list_display = ('seller', 'message', 'status', 'date_received')
    list_filter = ['status', 'date_received', 'seller']
    
admin.site.register(SupportMessage, SupportMessageAdmin)    