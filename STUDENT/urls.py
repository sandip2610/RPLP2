from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import notes_list

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.student_login, name='login'),
    path('san/', views.san, name='san' ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/<int:student_id>/', views.edit_profile, name='edit_profile'),
    path('success/', views.success_view, name='success'),
    path('chat_board', views.chat_board, name='chat_board'),
    path('edit_message/<int:message_id>/', views.edit_message, name='edit_message'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),  # Add this line
    path('video', views.video_list, name='video'),
    path('notes/', notes_list, name='notes_list'),
    path('admission/', views.student_admission, name='admission'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('change-password/', views.change_password, name='change_password'),
]