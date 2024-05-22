# forms.py
from django import forms
from .models import Book,Student
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'author', 'picture', 'category', 'download_link']



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'bio', 'phone_number', 'university_name', 'university_location', 'major_name']





class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Replace with your actual User model
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User  # Replace with your actual User model
        fields = ['username', 'password']

