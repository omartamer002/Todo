from rest_framework.response import Response
from .models import *
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
# GET all tasks
@api_view(['GET'])
def tasks(request):
  tasks = Task.objects.all()
  serializer = TaskSerializer(tasks, many=True)
  return Response(serializer.data)
# GET one task
@api_view(['GET'])
def getTask(request, pk):
  task = Task.objects.get(id=pk)
  serializer = TaskSerializer(task, many=False)
  return Response(serializer.data) 
# Creating a task
@api_view(['POST'])
def createTask(request):
  serializer = TaskSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data, status=status.HTTP_201_CREATED)
# Updating a task
@api_view(['PUT'])
def updateTask(request, pk):
  task = Task.objects.get(id=pk)
  serializer = TaskSerializer(instance=task, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data, status=status.HTTP_201_CREATED)
# Deleting a task
@api_view(['DELETE'])
def deleteTask(request, pk):
 task = Task.objects.get(id=pk)
 task.delete()
 return Response(status=status.HTTP_204_NO_CONTENT)
# Delete all tasks
@api_view(['DELETE'])
def deleteTasks(request):
  tasks = Task.objects.all()
  tasks.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)