from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def home(request):
    tasks = Task.objects.all().order_by('due_time')
    return render(request, 'tasks/home.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_time = request.POST.get('due_time')

        Task.objects.create(
            title=title,
            due_time=due_time,
            status='pending'
        )
        return redirect('/')

    return render(request, 'tasks/add_task.html')


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('/')


def toggle_task(request, id):
    task = get_object_or_404(Task, id=id)

    if task.status == 'done':
        task.status = 'pending'
    else:
        task.status = 'done'

    task.save()
    return redirect('/')