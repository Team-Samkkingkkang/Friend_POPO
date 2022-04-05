from django.urls import path
from . import views

app_name = "boardapp"

urlpatterns = [
    path('', views.BoardMainView, name="BoardMainView")
]
