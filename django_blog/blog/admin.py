from django.contrib import admin
from .models import Post
from .models import Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_date')
    list_filter = ('status', 'published_date', 'author')
    search_fields = ('title', 'content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "content", "created_at")
    search_fields = ("content", "author__username", "post__title")
    list_filter = ("created_at", "author")
