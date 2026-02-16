from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task
def home(request):
    tasks=Task.objects.filter(isCompleted=False).order_by('updatedAt')
    print(tasks)
    context={
        'tasks':tasks,
    }
    return render(request,'home.html',context)