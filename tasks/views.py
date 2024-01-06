from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task


def login_auth(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST["nome_user"]
        password = request.POST["senha_user"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('nome/senha inválidos!')


def ciar_nova_task(request):
    title = request.POST["title"]
    user = request.user

    nova_task = Task()
    nova_task.title = title
    nova_task.user_id = user
    nova_task.save()

    return redirect('home')


def deletar_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()

    return redirect('home')


def marcar_task(request, id):
    task = Task.objects.get(id=id)

    if task.done == False:
        task.done = True
    else:
        task.done = False

    task.save()

    return redirect('home')


@login_required(login_url="/")
def home(request):
    tasks = Task.objects.filter(user_id=request.user)
    context = {
        'tasks': tasks
    }
    return render(request, 'home.html', context)


def logout_user(request):
    logout(request)
    return redirect('login_auth')
