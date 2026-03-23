from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Kutilmoqda'),
        ('notified', 'Eslatildi'),
        ('done', 'Bajarildi'),
    ]

    title = models.CharField(max_length=200)
    due_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.title