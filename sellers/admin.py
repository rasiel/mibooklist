from mibooklist.books.models import *
from django.contrib import admin

class SellerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'screen_name', 'home_number',
                           'hide_phone', 'cellular_number',
                           'hide_cellular', 'account_status', 
                           'hide_email', 'location']})
    ]
    list_display = ('user', 'screen_name', 'account_status', 'signup_date')
    
admin.site.register(Seller, SellerAdmin)