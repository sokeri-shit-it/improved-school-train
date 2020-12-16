from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about-us.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'OOOOOOOOOOOOOOOOOOOO'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def sign_up(request):
    return render(request, 'main/sign_up.html', {'title': 'Войти'})


def personal_area(request):
    return render(request, 'main/personal_area.html', {'title': 'Личный кабинет'})


def register(request):
    return render(request, 'main/register.html', {'title': 'Зарегистрируй меня'})


def pay(request):
    return render(request, 'main/pay.html', {'title': 'Оплата'})
