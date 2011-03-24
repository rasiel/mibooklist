from models import Book

def book_count(request):	
    try:
        books = Book.objects.all().count()
    except Book.DoesNotExist:
        books = 0
    return {'book_count': books, }