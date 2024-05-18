from django.shortcuts import render
from .models import Todo

# Create your views here.
def home (req):
    todos = Todo.objects.all()
    return render(req, 'index.html',{
        'todos':todos,
    })

def completed (req):
    return render(req, 'completed.html')

def remaining (req):
    return render(req, 'remaining.html')

def add_task (req):
    return render(req, 'add_task.html')

def delete_task (req):
    return render(req, 'delete.html')

def task_detail (req):
    return render(req, 'task_detail.html')
