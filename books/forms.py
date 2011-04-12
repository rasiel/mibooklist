from django import forms
from models import Book
from sellers.models import Seller
from photologue.models import Photo
from django.template.defaultfilters import slugify
import random
from django.db.models import Max

########################################################################
class BookForm(forms.ModelForm):
    """Form for adding a new book"""
    seller = forms.CharField(widget=forms.HiddenInput())
    image = forms.CharField(widget=forms.HiddenInput(), required=False)
    new_image = forms.ImageField(required=False, help_text="Upload a valid jpg, png or gif image. Hint: you can search google for a book cover.")
    slug_url = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Book

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
    def clean_slug_url(self):
        slug = slugify(self.cleaned_data['title'])      
        try:
            slug_exists = Book.objects.filter(slug_url=slug)
        except Book.DoesNotExist:
            slug_exists = None
        if slug_exists:
            self.cleaned_data['slug_url'] = "%s-%s" %(slug, self.cleaned_data['seller'].id)
        else:
            self.cleaned_data['slug_url'] = slug
        return self.cleaned_data['slug_url']        
    
        
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
        rand_int = random.randint(1,99)
        if self.cleaned_data['image']:
            image = self.cleaned_data['image']
            image.image = self.cleaned_data['new_image']
            image.save()
            self.cleaned_data['image'] = image
        else:
            new_photo = Photo(image=self.cleaned_data['new_image'],
                          title= "%s %s %s" %(self.cleaned_data['title'], self.cleaned_data['seller'].user.username, rand_int),
                          title_slug = "%s_%s" %(self.cleaned_data['slug_url'], rand_int))
            new_photo.save()
            self.cleaned_data['image'] = new_photo
        return self.cleaned_data['image']
            
    
        
        
        
        
        
    
    