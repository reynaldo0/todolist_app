from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('completed/', views.completed, name = 'completed'),
    path('remaining/', views.remaining, name = 'remaining'),
    path('add_task/', views.add_task, name = 'add_task'),
    path('delete/<str:todo_id>', views.delete, name = 'delete'),
    path('detail/<str:todo_id>', views.task_detail, name = 'task_detail'),
    path('toggle_complete/<str:todo_id>', views.toggle_complete, name = 'toggle_complete'),
    path('remove_todo/<str:todo_id>', views.remove_todo, name = 'remove_todo'),
]
