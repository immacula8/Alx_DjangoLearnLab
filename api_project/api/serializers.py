from .models import Book
from rest_framework import serializers
from django.db import models

class BookSerializer(serializers.ModelSerializer):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)