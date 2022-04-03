from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accountapp'


urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]