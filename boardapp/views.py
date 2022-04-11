from django.shortcuts import render, redirect
from django.utils import timezone


def BoardMainView(request):
    return render(request, template_name='boardapp/BoardMainTemplate.html')

