from django.shortcuts import redirect, render

from .models import Task

#Display tasks
def index(request):
    task = Task.objects.all()
    return render(request, 'todo/index.html',{'task': task})

# Add a new task
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('index')
    return render(request, 'todo/add_task.html')

#Delete a task
def delete_task(request,task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')
    
