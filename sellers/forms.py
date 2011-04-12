from django import forms
from models import Seller, SupportMessage
from books.models import Book
from django.utils.translation import ugettext_lazy as _
from contact_form.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

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

class ContactSellerForm(ContactForm):
    to = forms.CharField(widget=forms.HiddenInput())
    book = forms.CharField(widget=forms.HiddenInput())
    
    subject_template_name = "contact_form/seller_form_subject.txt"
    
    template_name = 'contact_form/seller_form.txt'
    
    def clean_to(self):
        try:
            seller = Seller.objects.get(pk=self.cleaned_data['to'])
        except DoesNotExist:
            seller = None
        if seller:
            return seller
        else:
            raise forms.ValidationError("Could not send message to seller")
    
    def clean_book(self):
        try:
            book = Book.objects.get(pk=self.cleaned_data['book'])
        except Book.DoesNotExist:
            book = None
        if book:
            return book
        else:
            raise forms.ValidationError("Could not attach book to seller form.")
    
    def save(self,fail_silently=True):
        seller = Seller.objects.get(user=self.cleaned_data['to'].user.id)
        msg = SupportMessage(seller=seller, message=self.request.POST['body'])
        msg.save()
        self.recipient_list = [seller.user.email]
        send_mail(fail_silently=fail_silently,**self.get_message_dict())
        
class SupportForm(ContactForm):
    name = forms.CharField(widget=forms.HiddenInput(),required=False)
    email = forms.CharField(widget=forms.HiddenInput(),required=False)    
    
    def save(self,fail_silently=True):
        seller = Seller.objects.get(user=self.request.user.id)
        msg = SupportMessage(seller=seller, message=self.request.POST['body'])
        msg.save()
        send_mail(fail_silently=fail_silently,)
        


        
        
    
    