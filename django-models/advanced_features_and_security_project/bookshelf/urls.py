from django.urls import path
from . import views
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('', views.book_list, name='book_list'),
     path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),
]
