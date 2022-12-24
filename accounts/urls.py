from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from sheetupload import views

urlpatterns = [
    path('' ,views.home, name='dashboard'),
    path('course/' ,views.course),
    # path('sheet/' ,views.sheet),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sign-up/', views.SignUpView.as_view(), name = "sign-up"),
    # path('login', views.signin, name = "login"),
    path('signout', views.signout, name = "signout"),
    path('edit/' , views.edit),
    path('courseadd/', views.courseadd),
    path('upload/', views.simple_upload),
]

