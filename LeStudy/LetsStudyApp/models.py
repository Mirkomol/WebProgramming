from django.db import models

# models.py
from django.db import models


class Student(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True)
    university_name = models.CharField(max_length=100)
    university_location = models.CharField(max_length=255)
    major_name = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone_number})"


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    category = models.CharField(max_length=200, default='classic')
    download_link = models.URLField()

    def __str__(self):
        return self.book_name
