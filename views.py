from django.views.generic import simple
from books.models import Book, DISTRICT_CHOICES, CONDITION_CHOICES
from datetime import datetime
from django.views.generic.create_update import delete_object
from django.contrib.auth.models import User

def index(request):
    books = Book.objects.all().order_by('-created')[:6]
    date = datetime.now()
    return simple.direct_to_template(request, template='base.html', extra_context={'books': books, 'date': date})

def search(request):
    term = request.POST['searchterm']
    books = Book.objects.filter(title__icontains=term)
    return simple.direct_to_template(request, template='books/book_list.html', extra_context={'object_list': books, 'districts': DISTRICT_CHOICES, 'conditions': CONDITION_CHOICES, 'searchterm': term})

def advanced_search(request):
    title = request.POST['a_title']
    author = request.POST['a_author']
    school = request.POST['a_school']
    subject = request.POST['a_subject']
    publisher = request.POST['a_publisher']
    revision = request.POST['a_revision']
    edition = request.POST['a_edition']
    isbn = request.POST['a_isbn']
    books = Book.objects.filter(title__icontains=title,
                                author__icontains = author,
                                school__icontains = school,
                                course__icontains = subject,
                                revision__icontains = revision,
                                edition__icontains = edition,
                                isbn__icontains = isbn).order_by('-created')    
    return simple.direct_to_template(request, template='books/book_list.html', extra_context={'object_list': books, 'districts': DISTRICT_CHOICES, 'conditions': CONDITION_CHOICES, 'searchterm': 'advanced search'})
    

def sort(request):
    term = request.POST['sort_searchterm']
    fflag = ''
    sflag = ''
    tflag = ''
    if request.POST['sort_price'] != '':
        fflag = request.POST['sort_price']
    
    if request.POST['sort_condition'] != '':
        if fflag != '':
            sflag = request.POST['sort_condition']
        else:
            fflag = request.POST['sort_condition']
        
    if request.POST['sort_district'] != '':
        if sflag != '':
            tflag = request.POST['sort_district']
        else:
            if fflag == '':
                fflag = request.POST['sort_district']
            else:
                sflag = request.POST['sort_district']
    if fflag != '' and sflag != '' and tflag != '':
        books = Book.objects.filter(title__icontains=term).order_by(fflag, sflag, tflag)
    elif fflag != '' and sflag != '':
        books = Book.objects.filter(title__icontains=term).order_by(fflag, sflag)
    else:
        books = Book.objects.filter(title__icontains=term).order_by(fflag)
    return simple.direct_to_template(request, template='books/book_list.html', extra_context={'object_list': books, 'districts': DISTRICT_CHOICES, 'conditions': CONDITION_CHOICES, 'searchterm': term})

def delete_user(request, id):
    return delete_object(
        request,
        model = User,
        object_id = id,
        post_delete_redirect = '/accounts/register/',
        template_name = 'sellers/user_confirm_delete.html',
        login_required = True
    )