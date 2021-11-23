from django.http import HttpResponse
from django.shortcuts import render


def index_blog(request):
    return HttpResponse('Hello World')
