from django.db import models
from datetime import date

class Student(models.Model):

    name = models.CharField(max_length=100, default='Name')
    email = models.EmailField(unique=True, default='Email')
    phone_number = models.CharField(max_length=10, unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other')
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    password = models.CharField(max_length=28, default='Password')

    def __str__(self):
        return self.name

class NoticeBoard(models.Model):
    notice_no = models.AutoField(primary_key=True)
    notice = models.TextField()
    date = models.DateField(default=date.today)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
