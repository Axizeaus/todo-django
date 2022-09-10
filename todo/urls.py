from django.urls import path
from django.contrib import admin

from .views import DetailTodo, ListTodo

urlpatterns = [
    path('<int:pk>', DetailTodo.as_view(), name='todo_detail'),
    path('', ListTodo.as_view(), name='todo_list')
]
