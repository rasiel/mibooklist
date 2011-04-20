from mibooklist.books.models import *
from django.contrib import admin

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['seller', 'title','slug_url','isbn','author','edition','revision']}),
        ('Book Details', {'fields': ['description', 'school', 'course', 'location', 'district', 'condition', 'price', 'image', 'comments'], 'classes': ['collapse']}),
    ]
    prepopulated_fields = {'slug_url': ('title',)}
    list_display = ('title', 'seller', 'isbn', 'author', 'edition', 'revision')
    list_filter = ('seller', 'district', 'condition')
    search_fields = ('title', 'description')

admin.site.register(Book, BookAdmin)