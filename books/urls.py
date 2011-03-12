from django.conf.urls.defaults import *
from models import Book, DISTRICT_CHOICES, CONDITION_CHOICES
from views import detail, add, edit, delete
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, delete_object
from forms import BookForm

list_dict = {
    'queryset': Book.objects.all(),
    'paginate_by': 10,
    'extra_context': {'districts': DISTRICT_CHOICES, 'conditions': CONDITION_CHOICES}
}

urlpatterns = patterns('',
    (r'^page(?P<page>[0-9]+)/$', object_list, dict(list_dict)),
    (r'^add/$', add),
    (r'^edit/(?P<id>\d+)/$', edit),
    (r'^delete/(?P<id>\d+)/$', delete),
    (r'^(?P<slug>[-\w]+)/$', detail),    
)