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

class Admission(models.Model):
    student = models.OneToOneField('Student', on_delete=models.CASCADE)
    student_class = models.CharField(max_length=50)
    father_name = models.CharField(max_length=100)
    address = models.TextField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"Admission for {self.student.name}"

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

class Message(models.Model):
    sender = models.ForeignKey('Student', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)  # মেসেজ ফিল্ড
    file = models.FileField(upload_to='chat_files/', blank=True, null=True)  # ফাইল ফিল্ড
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.content:
            return f"{self.sender.name}: {self.content[:30]}"
        return f"{self.sender.name}: File"

class VideoContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title