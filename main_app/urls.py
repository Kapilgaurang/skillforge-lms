from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('courses/', views.courses, name='courses'),

    path('register/', views.register, name='register'),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('python-course/', views.python_course, name='python_course'),

    path('django-course/', views.django_course, name='django_course'),

    path('ai-course/', views.ai_course, name='ai_course'),

    path('certificates/', views.certificates, name='certificates'),

    path('certificate/', views.certificate, name='certificate'),

    path('chatbot/', views.chatbot, name='chatbot'),

    path('leaderboard/', views.leaderboard, name='leaderboard'),

]