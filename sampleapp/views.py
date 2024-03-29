from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo, assignee
from django.contrib.staticfiles.templatetags.staticfiles import static
from sklearn.externals import joblib
from django.conf import settings

def index(request):
    if request.method == 'POST':
        return redirect('sampleapp:home')
    return render(request, 'sampleapp/index.html')

def home(request):
    # to check method of request GET or POST
    if request.method == 'POST':
        # fetching values from input boxes
        title = request.POST['title']
        des = request.POST['des']

        # creating object and saving it with fetched values
        todo = Todo(title=title,des=des).save()

        # rendering the template with the todo value
        return render(request, 'sampleapp/home.html', {'todo': todo})      

    # List of all the objects present in Database
    todoList = Todo.objects.all()
    return render(request, 'sampleapp/home.html', {'todoList': todoList})

def detail(request, id):
    # Try to fetch the object with given id
    try: 
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        # if object not found redirect to home page
        return redirect('sampleapp:home')

    # Check if the request method is get or post
    if request.method == 'POST':
        # fetching value from input boxes and storing them as fields of the object
        todo.title = request.POST['title']
        todo.des = request.POST['des']
        # saving the objects with new fields
        todo.save()   
    
    # render the template with the object having given id
    return render(request, 'sampleapp/detail.html', {'todo': todo})

def profile(request, id):
    person = get_object_or_404(assignee, id=id)
    return render(request, 'sampleapp/profile.html', {'person': person})

def mlrocks(request):
    if request.method == 'POST':
        input_list = list()
        age = int(request.POST['age'])
        estimate = int(request.POST['est'])
        input_list.append([age,estimate])
        print(input_list)
        print(static('css/abc1.css'))
        model = joblib.load('sampleapp/static/objects/classifier.yml')
        sc = joblib.load('sampleapp/static/objects/sc.yml')

        x = input_list

        X_test = sc.transform(x)

        predict = model.predict(X_test)
        if predict[0] == 0:
            out = "Not Purchased"
        else:
            out = "Purchased"
        return render(request, 'sampleapp/ml.html', {'out': out})

    return render(request, 'sampleapp/ml.html')