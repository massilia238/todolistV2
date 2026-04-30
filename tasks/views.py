from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect('index')

    tasks = Task.objects.all().order_by('-created')
    return render(request, "tasks/index.html", {"tasks": tasks})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')