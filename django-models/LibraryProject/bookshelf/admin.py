from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these fields in admin list
    search_fields = ('title', 'author')                     # Enable search by title and author
    list_filter = ('publication_year',)                     # Add a filter sidebar for publication year
