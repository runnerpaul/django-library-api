from django.urls import path
from .views import ListTodo, DetialTodo

urlpatterns = [
    path('<int:pk>/', DetialTodo.as_view()),
    path('', ListTodo.as_view()),
]