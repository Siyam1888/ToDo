from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def index(request):
    form = TaskForm()
    task = Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'task/task_list.html', {'form': form, 'tasks': task})


def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'task/update.html', {'form': form})


def delete(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == "POST":
        item = Task.objects.get(id=pk)
        item.delete()
        return redirect('/')

    return render(request, 'task/delete.html', {'item': item})


