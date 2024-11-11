from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm
from .models import Student, NoticeBoard, Contact
from .forms import EditProfileForm
from .forms import ContactForm

def home(request):
    notices = NoticeBoard.objects.all()
    return render(request, 'home.html', {'notices': notices})

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        dob = request.POST['dob']
        gender = request.POST['gender']
        password = request.POST['password']
        photo = request.FILES['photo'] if 'photo' in request.FILES else None
        student = Student(name=name, email=email, phone_number=phone_number, gender=gender, dob=dob, password=password, photo=photo)
        student.save()
        return redirect('login')
    return render(request, 'register.html')

def student_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                student = Student.objects.get(email=email, password=password)
                request.session['student_id'] = student.id
                return redirect('san')
            except Student.DoesNotExist:
                return render(request, 'login.html', {'form': form, 'error': 'Email or Password is Wrong!'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def profile(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')
    student = Student.objects.get(id=student_id)
    return render(request, 'profile.html', {'student': student})

def san(request):
    return render(request, 'san.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def edit_profile(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=student)
    return render(request, 'edit_profile.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')