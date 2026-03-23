from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.add_task),
    path('delete/<int:id>/', views.delete_task),
    path('toggle/<int:id>/', views.toggle_task),
]