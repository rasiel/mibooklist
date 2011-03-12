from mibooklist.books.models import *
from django.contrib import admin

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['seller', 'title','slug_url','isbn','author','edition','revision']}),
        ('Book Details', {'fields': ['description', 'school', 'course', 'location', 'district', 'condition', 'price', 'image', 'comments'], 'classes': ['collapse']}),
    ]
    prepopulated_fields = {'slug_url': ('title',)}
    list_display = ('seller', 'title', 'isbn', 'author', 'edition', 'revision')

admin.site.register(Book, BookAdmin)