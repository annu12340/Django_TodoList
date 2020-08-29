from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .forms import TodoForm
from .models import Blog


def home(request):
    form = TodoForm()
    print(form)
    todos = Blog.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            render(request, 'home.html')
    return render(request, 'home.html', {'form': form, 'todos': todos})


def update(request, todo_id):
    todo = Blog.objects.get(id=todo_id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return  render(request, 'home.html')
    return render(request, 'update.html', {'form': form, 'todo': todo})


def delete(request, todo_id):
    if request.method == 'POST':
        Blog.objects.get(id=todo_id).delete()
        return render(request, 'home.html')