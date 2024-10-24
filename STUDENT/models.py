from django.db import models
from datetime import date

class Student(models.Model):
    name = models.CharField(max_length=100, default='Name')
    email = models.EmailField(unique=True, default='Email')
    phone_number = models.CharField(max_length=10, unique=True)
    dob = models.DateField()
    password = models.CharField(max_length=28, default='Password')

    def _str_(self):
        return self.name

class NoticeBoard(models.Model):
    notice_no = models.AutoField(primary_key=True)
    notice = models.TextField()
    date = models.DateField(default=date.today)