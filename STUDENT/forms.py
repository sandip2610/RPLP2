from django import forms
from .models import Student
from .models import NoticeBoard
from .models import Contact
from .models import Admission


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone_number', 'gender', 'dob', 'photo','password']
        labels = {
            'name': 'name',
            'email': 'email',
            'mobile_number': 'mobile_number',
            'gender': 'gender',
            'dob': 'dob',
            'photo': 'photo',
            'password': 'password',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'enter your email'})
    )
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter your password'})
    )

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['student_class', 'subject', 'father_name', 'address']

class NoticeBoardForm(forms.ModelForm):
    class Meta:
        model = NoticeBoard
        fields = ['notice_no', 'notice', 'date']
        labels = {
            'notice_no': 'notice_no',
            'notice': 'notice',
            'data': 'data',
        }

class EditProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Student
        exclude = ['phone_number', 'password']
        fields = ['name', 'email', 'dob', 'phone_number', 'gender', 'photo', 'password']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

class PasswordResetForm(forms.Form):
        email = forms.EmailField()
        dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)))