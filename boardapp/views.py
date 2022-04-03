from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Board, Comment


def index(request):

    question_list = Board.objects.order_by('-board_date')
    context = {'question_list': question_list}
    return render(reqeust, '')
