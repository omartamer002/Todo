from django.urls import path
from .views import *
# These are the endpoints
urlpatterns = [
  path('', tasks, name='tasks'),
  path('<int:pk>/', getTask, name='getTask'),
  path('create/', createTask, name='createTask'),
  path('<int:pk>/update/', updateTask, name='updateTask'),
  path('<int:pk>/delete/', deleteTask, name='deleteTask'),
  path('delete/', deleteTasks, name='deleteTasks'),
]