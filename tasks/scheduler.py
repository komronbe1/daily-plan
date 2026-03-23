from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from .models import Task


def check_tasks():
    now = timezone.now()

    tasks = Task.objects.filter(
        due_time__lte=now,
        status='pending'
    )

    for task in tasks:
        print(f"🔔 ESLATMA: {task.title}")

        # endi notified qilamiz
        task.status = 'notified'
        task.save()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_tasks, 'interval', minutes=1)
    scheduler.start()