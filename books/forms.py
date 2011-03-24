from django import forms
from models import Book
from sellers.models import Seller
from photologue.models import Photo
from django.template.defaultfilters import slugify
import random

########################################################################
class BookForm(forms.ModelForm):
    """Form for adding a new book"""
    seller = forms.CharField(widget=forms.HiddenInput())
    image = forms.CharField(widget=forms.HiddenInput(), required=False)
    new_image = forms.ImageField(required=False, help_text="Upload a valid jpg, png or gif image. Hint: you can search google for a book cover.")
    slug_url = forms.CharField(widget=forms.HiddenInput())
    
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
        rand_int = random.randint(1,99)
        if self.cleaned_data['title']:
            slug_title = slugify(self.cleaned_data['title'])
        else:
            slug_title = False
        if slug_title and self.cleaned_data['new_image'] and self.cleaned_data['image']:
            new_photo = Photo.objects.get(title_slug = "%s_%s_%s" %(slug_title, self.cleaned_data['seller'],rand_int))
            new_photo.image = self.cleaned_data['new_image']
            new_photo.save()
            
        if slug_title and self.cleaned_data['new_image']:            
            new_photo = Photo(image=self.cleaned_data['new_image'],
                          title= "%s_%s_%s" %(self.cleaned_data['title'], self.cleaned_data['seller'], rand_int),
                          title_slug = "%s_%s_%s" %(slug_title, self.cleaned_data['seller'], rand_int))
            new_photo.save()        
        
        if new_photo:
            self.cleaned_data['image'] = new_photo
        else:
            return None    
    
        
        
        
        
        
    
    