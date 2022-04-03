from django.urls import path

from . import views

app_name = 'popoapp'

urlpatterns = [
    path('index/', views.index, name="index")
]