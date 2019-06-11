from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo

def index(request):
    if request.method == 'POST':
        return redirect('home1')
    return render(request, 'index.html')

def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        des = request.POST['des']
        todo = Todo(title=title,des=des).save()
        return render(request, 'home.html', {'todo': todo})      

    todoList = Todo.objects.all()
    return render(request, 'home.html', {'todoList': todoList})

def detail(request, id):
    try: 
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return redirect('home')
    # todo = get_object_or_404(Todo, id=id)
    return render(request, 'home.html', {'todo': todo})
