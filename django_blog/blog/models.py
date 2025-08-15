from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
class Comment(models.Model):
    post = models.ForeignKey(
        'Post',  # The Post model (string to avoid circular import issues)
        on_delete=models.CASCADE,  # If a post is deleted, delete its comments
        related_name='comments'    # Allows post.comments.all() access
    )
    author = models.ForeignKey(
        User,  # Django's built-in user model
        on_delete=models.CASCADE   # If user is deleted, delete their comments
    )
    content = models.TextField()  # Comment text
    created_at = models.DateTimeField(auto_now_add=True)  # Created time
    updated_at = models.DateTimeField(auto_now=True)      # Updated time

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
