from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def home (req):
    todos = Todo.objects.all().order_by('due_date')

    return render(req, 'index.html',{
        'todos': todos, 
    })

def completed (req):
    completed_todos = Todo.objects.filter(completed=True)

    return render(req, 'completed.html',{
        'todos':completed_todos,
    })

def remaining (req):
    remaining_todos = Todo.objects.filter(completed=False)

    return render(req, 'remaining.html',{
        'todos':remaining_todos,
    })

def add_task (req):
    if req.method == "POST":
        title = req.POST.get('title') 
        desc = req.POST.get('desc') 
        due_date = req.POST.get('due_date') 
        due_time = req.POST.get('due_time') 
        completed = False

        if title != "" and due_date != "" and due_time != "":
            todo = Todo(
                title = title,
                desc = desc,
                due_date = due_date,
                due_time = due_time,
                completed = completed
            )
            todo.save()
            return redirect ('home')
    else:
        return render(req, 'add_task.html')
    return render(req, 'add_task.html')

def delete_task (req):
    return render(req, 'delete.html')

def task_detail (req, todo_id):
    todo = Todo.objects.get(id = todo_id)
    return render(req, 'task_detail.html',{
        "todo": todo,
    })
