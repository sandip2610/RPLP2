from django.contrib import admin
from .models import Student
from .models import NoticeBoard
from .models import Contact

admin.site.register(Student)
admin.site.register(NoticeBoard)
admin.site.register(Contact)