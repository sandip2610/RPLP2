from django import forms
from .models import Student
from .models import NoticeBoard
from .models import Contact

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

class EditProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Student
        fields = ['name', 'email', 'dob', 'phone_number', 'gender', 'photo', 'password']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']