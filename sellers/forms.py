from django import forms
from models import Seller, SupportMessage
from django.utils.translation import ugettext_lazy as _
from contact_form.forms import ContactForm
from django.core.mail import send_mail

########################################################################
class SellerForm(forms.ModelForm):
    """Custom Form for seller profile"""
    first_name = forms.CharField(help_text=_(u'Not displayed, for internal use only.'), 
                                error_messages={'required': _("First Name is required.")})
    last_name = forms.CharField(help_text=_(u'Not displayed, for internal use only.'), 
                                error_messages={'required': _("Last Name is required.")})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(maxlength=75)),
                             label=_("Email address"))
    class Meta:
        model = Seller
        exclude = ('user', 'account_status',)
        
class SupportForm(ContactForm):
    name = forms.CharField(widget=forms.HiddenInput(),required=False)
    email = forms.CharField(widget=forms.HiddenInput(),required=False)
    
    def save(self,fail_silently=False):
        seller = Seller.objects.get(user=self.request.user.id)
        msg = SupportMessage(seller=seller, message=self.request.POST['body'])
        msg.save()
        send_mail(fail_silently=fail_silently, **self.get_message_dict())
        


        
        
    
    