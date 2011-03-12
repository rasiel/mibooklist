from django import forms
from models import Seller

########################################################################
class SellerForm(forms.ModelForm):
    """Custom Form for seller profile"""
    class Meta:
        model = Seller
        exclude = ('user', 'account_status',)
        


        
        
    
    