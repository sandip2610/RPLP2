from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, ContactForm, AdmissionForm, EditProfileForm, PasswordResetForm
from .models import Student, NoticeBoard, Message, VideoContent, Contact, Admission
from django.http import HttpResponseForbidden
from django.core.mail import send_mail
import random
from django.contrib import messages

def home(request):
    notices = NoticeBoard.objects.all()
    return render(request, 'home.html', {'notices': notices})

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        dob = request.POST.get('dob', '').strip()
        gender = request.POST.get('gender', '').strip()
        password = request.POST.get('password', '').strip()
        photo = request.FILES.get('photo')
        if not all([name, email, phone_number, dob, gender, password]):
            messages.error(request, 'Please fill all the required fields.')
            return render(request, 'register.html')
        student = Student(
            name=name,
            email=email,
            phone_number=phone_number,
            gender=gender,
            dob=dob,
            password=password,
            photo=photo
        )
        student.save()
        messages.success(request, 'Registration successful! You can now log in.')
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
                return redirect('profile')
            except Student.DoesNotExist:
                return render(request, 'login.html', {'form': form, 'error': 'Email or Password is Wrong!'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            dob = form.cleaned_data['dob']
            try:
                student = Student.objects.get(email=email, dob=dob)
                temp_password = str(random.randint(100000, 999999))
                student.password = temp_password
                student.save()
                send_mail(
                    'Temporary Password',
                    f'Your temporary password is: {temp_password}. Please log in and change your password.',
                    'your_email@example.com',
                    [email],
                    fail_silently=False,
                )
                return render(request, 'password_reset.html',
                              {'form': form, 'success':'A temporary password has been sent to your email.'})
            except Student.DoesNotExist:
                return render(request, 'password_reset.html',
                              {'form': form, 'error': 'Invalid email or date of birth.'})
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        student_id = request.session.get('student_id')
        if student_id:
            student = Student.objects.get(id=student_id)
            if student.password != old_password:
                messages.error(request, 'Old password does not match.')
                return render(request, 'change_password.html')
            if new_password != confirm_password:
                messages.error(request, 'New password and confirm password do not match.')
                return render(request, 'change_password.html')
            student.password = new_password
            student.save()
            messages.success(request, 'Password changed successfully. Please log in again.')
            return redirect('login')
        else:
            messages.error(request, 'User not logged in.')
            return redirect('login')
    return render(request, 'change_password.html')

def profile(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')
    try:
        student = Student.objects.get(id=student_id)
        admission = Admission.objects.get(student=student)
    except Student.DoesNotExist:
        return redirect('login')
    except Admission.DoesNotExist:
        admission = None
    return render(request, 'profile.html', {'student': student, 'admission': admission})

def student_admission(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return redirect('login')
    if Admission.objects.filter(student=student).exists():
        return render(request, 'success.html', {
            'message': 'You have already completed the admission process.',
            'student': student
        })
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            admission = form.save(commit=False)
            admission.student = student
            admission.save()
            student.is_admitted = True
            student.save()
            return redirect('success')
    else:
        form = AdmissionForm()
    return render(request, 'student_admission.html', {'form': form, 'student': student})

def chat_board(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        content = request.POST.get('content')
        uploaded_file = request.FILES.get('file')
        if content or uploaded_file:
            message = Message.objects.create(sender=student, content=content)
            if uploaded_file:
                message.file = uploaded_file
                message.save()
        return redirect('chat_board')
    messages = Message.objects.all().order_by('-timestamp')
    return render(request, 'chat_board.html', {'messages': messages})

def edit_message(request, message_id):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')
    student = Student.objects.get(id=student_id)
    message = get_object_or_404(Message, id=message_id)
    if message.sender != student:
        return HttpResponseForbidden("You are not allowed to edit this message.")
    if message.file:
        return HttpResponseForbidden("File messages cannot be edited.")
    if request.method == "POST":
        new_content = request.POST.get('new_content')
        if new_content:
            message.content = new_content
            message.save()
            return redirect('chat_board')
    return render(request, 'edit_message.html', {'message': message})

def delete_message(request, message_id):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')
    student = Student.objects.get(id=student_id)
    message = get_object_or_404(Message, id=message_id)
    if message.sender != student:
        return HttpResponseForbidden("You are not allowed to delete this message.")
    message.delete()
    return redirect('chat_board')

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

def video_list(request):
    videos = VideoContent.objects.all()
    return render(request, 'video.html', {'videos': videos})