# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic import simple
from models import Seller
from books.models import Book

@login_required
def profile(request):
    try:
        seller = Seller.objects.get(user=request.user.id)
    except Seller.DoesNotExist:
        seller = None
    if seller:
        book_count = Book.objects.filter(seller=seller.id).count()
    else:
        book_count = 0
    return simple.direct_to_template(request, 
                                     template='sellers/profile.html', 
                                     extra_context={'seller': seller,
                                                    'book_count': book_count})

@login_required
def books(request):
    try:
        seller = Seller.objects.get(user=request.user.id)
    except Seller.DoesNotExist:
        seller = None
        
    if seller:
        try:
            books = Book.objects.filter(seller=seller.id)
        except Book.DoesNotExist:
            books = None
    else:
        books = None
        
    return simple.direct_to_template(request, 
                                     template='sellers/books.html', 
                                     extra_context={'seller': seller, 
                                                    'books': books})
    