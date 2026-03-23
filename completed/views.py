from django.shortcuts import render
from tasks.models import Task

def completed_tasks(request):
    tasks = Task.objects.filter(status='done')
    return render(request, 'completed/list.html', {'tasks': tasks})