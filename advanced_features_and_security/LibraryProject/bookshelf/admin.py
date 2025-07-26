

#@admin.register(Book)
#class BookAdmin(admin.ModelAdmin):
 #   list_display = ('title', 'author', 'publication_year')  # Show these fields in admin list
  #  search_fields = ('title', 'author')                     # Enable search by title and author
   # list_filter = ('publication_year',)                     # Add a filter sidebar for publication year

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Info'), {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Additional Info'), {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
