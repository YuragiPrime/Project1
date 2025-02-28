from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from .models import Musician, Tank, Student, Course
from .form import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

@require_http_methods(["GET", "POST"])
def index(request):
    return render(request, 'index.html')

def home(request):
    return HttpResponse("Welcome to the Home Page!")

def about(request):
    return render(request, 'about.html')

def table(request):
    musicians = Musician.objects.all()  # Витягуємо всі об'єкти
    return render(request, 'table.html', {'musicians': musicians})

def tank_table(request):
    tanks = Tank.objects.all()  # Витягуємо всі об'єкти
    return render(request, 'tank_table.html', {'tanks': tanks})

def form(request):
    return render(request, 'form.html')

def login_page(request):
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})

def login_p(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index.html")
            messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"login_form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index.html")

def admin_page(request):
    return render(request, 'admin_page.html')

def add_product(request):
    if request.method == 'POST':
        # Обробка даних форми
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        # Збереження продукту в базу даних (залежить від вашої моделі)
        return HttpResponse("Product added successfully!")
    return render(request, 'add_product.html')

def student_courses(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'student_courses.html', {'student': student})

def course_students(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course_students.html', {'course': course})

def by_rubric(request, rubric_id):
    return render(request, 'by_rubric.html', {'rubric_id': rubric_id})

class HomePageView(TemplateView):
    template_name = 'index2.html'

class AboutPageView(TemplateView):
    template_name = 'about2.html'

class DataPageView(TemplateView):
    def get(self, request, **kwargs):
        context = {
            'data': [
                {
                    'name': 'Celeb 1',
                    'worth': '3567892'
                },
                {
                    'name': 'Celeb 2',
                    'worth': '23000000'
                },
                {
                    'name': 'Celeb 3',
                    'worth': '1000007'
                },
                {
                    'name': 'Celeb 4',
                    'worth': '456789'
                },
                {
                    'name': 'Celeb 5',
                    'worth': '7890000'
                },
                {
                    'name': 'Celeb 6',
                    'worth': '12000456'
                },
                {
                    'name': 'Celeb 7',
                    'worth': '896000'
                },
                {
                    'name': 'Celeb 8',
                    'worth': '670000'
                }
            ]
        }
        return render(request, 'data.html', context)