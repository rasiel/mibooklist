# Create your views here.
from models import Book
from forms import BookForm
from sellers.models import Seller
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object, delete_object
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from sellers.forms import ContactSellerForm

def detail(request, slug):
    book = Book.objects.get(slug_url = slug)
    book.increase_views()
    other_books = Book.objects.filter(seller__id = book.seller.id).exclude(slug_url=slug)
    return object_detail(
        request,
        queryset = Book.objects.all(),
        slug_field = 'slug_url',
        slug = slug,
        template_name = 'books/book_detail.html',
        extra_context = {'other_books': other_books, 
                         'sellercontact_form': ContactSellerForm(request=request,initial={'to': book.seller.id, 'book': book.id})}
    )

@login_required
def add(request):
    """View to add a book, we will check if the seller is active first"""
    try:
        seller = Seller.objects.get(user=request.user.id)
    except Seller.DoesNotExist:
        seller = None
    if seller and seller.account_status == 'AC':
        can_add_book = True
        seller_id = seller.id
    else:
        can_add_book = False
        seller_id = None
        
    if request.method == 'POST': # If the form has been submitted...
        form = BookForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return redirect('/accounts/books/') # Redirect after POST
    else:
        form = BookForm(initial={'seller': seller_id}) # An unbound form

    return render_to_response('books/book_form.html', {
        'form': form,
        'can_add_book': can_add_book
    },context_instance=RequestContext(request))

@login_required
def edit(request, id):
    """Edit a book, using the passed id"""
    book = Book.objects.get(pk=id)
    if request.method == 'POST': # If the form has been submitted...
        form = BookForm(request.POST, request.FILES, instance=book) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            form.save()
            return redirect('/accounts/books/') # Redirect after POST
    else:
        form = BookForm(instance=book) # Lets bound the form

    return render_to_response('books/book_form.html', {
        'form': form,
        'can_add_book': True
    },context_instance=RequestContext(request))

def delete(request, id):
    return delete_object(
        request,
        model = Book,
        object_id = id,
        post_delete_redirect = '/accounts/books/',
        login_required = True
    )
        