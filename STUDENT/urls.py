from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
]