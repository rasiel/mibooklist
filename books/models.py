from django.db import models
from mibooklist.sellers.models import Seller
from photologue.models import Photo

DISTRICT_CHOICES = (
    ('CZ', 'Corozal'),
    ('OW', 'Orange Walk'),
    ('BZ', 'Belize'),
    ('CY', 'Cayo'),
    ('SC', 'Dangriga'),
    ('TO', 'Toledo')
)

CONDITION_CHOICES = (
    ('NW', 'NEW'),
    ('EX', 'EXCELLENT'),
    ('GD', 'GOOD'),
    ('FR', 'FAIR')
)

# Create your models here.
class Book (models.Model):
    seller = models.ForeignKey(Seller,related_name="book_seller")
    title = models.CharField(max_length=100)
    slug_url = models.SlugField()
    description = models.TextField(blank=True,null=True)
    publisher = models.CharField(max_length=100)
    isbn = models.CharField(max_length=25)
    author = models.CharField(max_length=100)
    edition = models.CharField(max_length=20, blank=True, null=True)
    revision = models.CharField(max_length=20, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    course = models.CharField(max_length=25, blank=True, null=True)
    location = models.CharField(max_length=50, help_text="without being specific general area where book is")
    district = models.CharField(max_length=2,choices=DISTRICT_CHOICES)
    condition = models.CharField(max_length=2, choices=CONDITION_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ForeignKey(Photo, blank=True, null=True)
    comments = models.TextField(help_text="In this box state your payment options and arrangement on getting the book, etc.")
    created = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0, editable=False)
    
    class Meta:
        get_latest_by = '-created'
        ordering = ['-created']

    def __unicode__(self):
        return self.title
    
    def increase_views(self):
        self.views += 1
        models.Model.save(self)

    def get_absolute_url(self):
        return "/books/%s/" % (self.slug_url)