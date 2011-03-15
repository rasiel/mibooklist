from django import forms
from models import Book
from sellers.models import Seller
from photologue.models import Photo
from django.template.defaultfilters import slugify

########################################################################
class BookForm(forms.ModelForm):
    """Form for adding a new book"""
    seller = forms.CharField(widget=forms.HiddenInput())
    image = forms.CharField(widget=forms.HiddenInput(), required=False)
    new_image = forms.ImageField(required=False)
    slug_url = forms.SlugField(help_text="This is a unique, search engine friendly URL")
    
    class Meta:
        model = Book
        
    #----------------------------------------------------------------------
    def clean_seller(self):
        try:
            seller = Seller.objects.get(pk=self.cleaned_data['seller'])
        except Seller.DoesNotExist:
            seller = None
        if seller:
            return seller
        else:
            raise forms.ValidationError("Could not attach book to seller")
        
    #----------------------------------------------------------------------
    def clean_image(self):
        """"""
        if self.cleaned_data['image']:
            try:
                image = Photo.objects.get(pk=self.cleaned_data['image'])
            except Photo.DoesNotExist:
                image = None
            return image
        else:
            return None
        
    def clean_new_image(self):
        """Let's take the uploaded image, create a new photo and bind to 
        the image field in model"""
        new_photo = None
        if self.cleaned_data['new_image'] and self.cleaned_data['image']:
            new_photo = Photo.objects.get(title_slug = slugify(self.cleaned_data['title']))
            new_photo.image = self.cleaned_data['new_image']
            new_photo.save()
            
        if self.cleaned_data['new_image']:
            slug_title = slugify(self.cleaned_data['title'])
            new_photo = Photo(image=self.cleaned_data['new_image'],
                          title= "%s_%s" %(self.cleaned_data['title'], self.cleaned_data['seller']),
                          title_slug = "%s_%s" %(slug_title, self.cleaned_data['seller']))
            new_photo.save()        
        
        if new_photo:
            self.cleaned_data['image'] = new_photo
        else:
            return None    
    
        
        
        
        
        
    
    