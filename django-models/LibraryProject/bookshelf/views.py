from django.shortcuts import render
from .models import Book
from relationship_app.models import Book
from django.contrib.auth.decorators import permission_required


def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    # handle adding a book
    ...

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    # handle editing a book
    ...

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    # handle deleting a book
    ...

