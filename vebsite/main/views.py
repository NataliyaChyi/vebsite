from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about_us(request):
    return render(request, 'main/about.html')
# Create your views here.
