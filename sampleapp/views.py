from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo, assignee

def index(request):
    if request.method == 'POST':
        return redirect('home1')
    return render(request, 'index.html')

def home(request):
    # to check method of request GET or POST
    if request.method == 'POST':
        # fetching values from input boxes
        title = request.POST['title']
        des = request.POST['des']

        # creating object and saving it with fetched values
        todo = Todo(title=title,des=des).save()

        # rendering the template with the todo value
        return render(request, 'home.html', {'todo': todo})      

    # List of all the objects present in Database
    todoList = Todo.objects.all()
    return render(request, 'home.html', {'todoList': todoList})

def detail(request, id):
    # Try to fetch the object with given id
    try: 
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        # if object not found redirect to home page
        return redirect('home')

    # Check if the request method is get or post
    if request.method == 'POST':
        # fetching value from input boxes and storing them as fields of the object
        todo.title = request.POST['title']
        todo.des = request.POST['des']
        # saving the objects with new fields
        todo.save()   
    
    # render the template with the object having given id
    return render(request, 'detail.html', {'todo': todo})

def profile(request, id):
    person = get_object_or_404(assignee, id=id)
    return render(request, 'profile.html', {'person': person})