
from django.shortcuts import render
from todo.models import Task

 
def home(request):
    tasks = Task.objects.filter(isCompleted = False).order_by('-updatedAt')
    Completed = Task.objects.filter(isCompleted = True)
    context = {
        'tasks' : tasks,
        'Completed' : Completed
    }
    return(render(request, 'home.html', context))