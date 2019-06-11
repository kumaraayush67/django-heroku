from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

def index(request):
    if request.method == 'POST':
        return redirect('home1')
    return render(request, 'index.html')

def home(request, id=None):
    if request.method == 'POST':
        title = request.POST['title']
        des = request.POST['des']
        todo = Todo(title=title,des=des).save()
        return render(request, 'home.html', {'todo': todo})      

    todoList = Todo.objects.all()
    return render(request, 'home.html', {'todoList': todoList})


def base(request):
    return render(request, 'todos.html')
