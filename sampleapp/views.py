from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        return redirect('home1')
    return render(request, 'index.html')

def home(request, id=None):
    if request.method == 'POST':
        return render(request, 'home.html', {'method': "POST"})
    return render(request, 'home.html', {'method': "GET", "id": id})


def base(request):
    return render(request, 'base.html')
