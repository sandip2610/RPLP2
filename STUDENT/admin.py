from django.contrib import admin
from .models import Student
from .models import NoticeBoard
from .models import Contact
from .models import VideoContent
from .models import Admission
from .models import Note


admin.site.register(Student)
admin.site.register(Admission)
admin.site.register(NoticeBoard)
admin.site.register(Contact)
admin.site.register(VideoContent)
admin.site.register(Note)