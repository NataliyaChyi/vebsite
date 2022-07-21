from django.shortcuts import render
from django.http import HttpResponse
from . models import Task
from . forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('title')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about_us(request):
    return render(request, 'main/about.html')


def create(request):
    form = TaskForm()
    context = {'form': form}
    return render(request, 'main/create.html', context)


def examples(request):
    form = TaskForm()
    context = {'form': form}
    return render(request, 'main/examples.html', context)


# Create your views here.
