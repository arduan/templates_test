from django.http import HttpResponse
from django.shortcuts import render


def index_blog(request):
    return HttpResponse('Привет Мир')


def blog(request):
    return HttpResponse('Привет Виталий')
