from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from .models import Book, Student
from .forms import BookForm, StudentForm
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace with your desired URL after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'LetsStudyApp/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace with your desired URL after login
    else:
        form = CustomAuthenticationForm()
    return render(request, 'LetsStudyApp/login.html', {'form': form})



class homeView(ListView):
    model = Student
    template_name = 'LetsStudyApp/home.html'
    context_object_name = 'students'

    def get_queryset(self):
        query = self.request.GET.get('item_search')
        if query:
            return Student.objects.filter(major_name__icontains=query)
        else:
            return Student.objects.all()



class StudentDetailView(DetailView):
    model = Student  # Specify the model for the detailed view
    template_name = 'LetsStudyApp/student_detail.html'  # Specify the template for rendering
    context_object_name = 'student'



def game(request):
    return render(request, 'LetsStudyApp/game.html')



class libraryView(ListView):
    model = Book
    template_name = 'LetsStudyApp/library.html'
    context_object_name = 'books'
    paginate_by = 6

    def get_queryset(self):

        query = self.request.GET.get('item_search')

        if query:
            return Book.objects.filter(category__icontains=query)
        else:
            return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)

        context['books'] = books
        return context




@login_required
def addBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('library')
    else:
        form = BookForm()

    return render(request, 'LetsStudyApp/add_form.html', {'forms': form})



@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'students_list' with your actual URL name for the students list page
    else:
        form = StudentForm()

    return render(request, 'LetsStudyApp/add_student.html', {'form': form})
