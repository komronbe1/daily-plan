from django.apps import AppConfig
import os

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

    def ready(self):
        if os.environ.get('RUN_MAIN') != 'true':
            return

        from .scheduler import start
        start()