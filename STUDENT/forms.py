from django import forms
from .models import Student
from .models import NoticeBoard

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone_number', 'dob', 'password']

        labels = {
            'name': 'name',
            'email': 'email',
            'mobile_number': 'mobile_number',
            'dob': 'dob',
            'password': 'password',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(label="email")
    password = forms.CharField(widget=forms.PasswordInput, label="password")

class NoticeBoardForm(forms.ModelForm):
    class Meta:
        model = NoticeBoard
        fields = ['notice_no', 'notice', 'date']
        labels = {
            'notice_no': 'notice_no',
            'notice': 'notice',
            'data': 'data',
        }
