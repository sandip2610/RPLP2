from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, LoginForm
from .models import Student, NoticeBoard

def home(request):
    notices = NoticeBoard.objects.all()
    return render(request, 'home.html', {'notices': notices})

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = Student.objects.get(email=email)
                if user.password == password:
                    return redirect('san')
            except Student.DoesNotExist:
                return render(request, 'login.html', {'form': form, 'error': 'Email or password is wrong!'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def san(request):
    return render(request, 'san.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')