from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task


# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.isCompleted = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.isCompleted = False
    task.save()
    return redirect('home')

def removeTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

def editTask(request, pk):
    getTask = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        newTask = request.POST['task']
        getTask.task = newTask
        getTask.save()
        return redirect('home')
    else:
        context = {
            "getTask" : getTask,
        }
        return render(request, 'editTask.html', context)