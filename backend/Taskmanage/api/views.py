from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserSerializer, TaskSerializer
from .models import User, Task 
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

class UserViews:
    @api_view(['POST'])
    def registerUser(request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
    
    @api_view(['GET'])
    def getUsers(request):
        allUsers = User.objects.all()
        serializer = UserSerializer(allUsers, many=True)
        return Response(serializer.data)
        

    @api_view(['POST'])
    def login(request):
        object = User.objects.get(username=request.data["username"], password=request.data["password"])
        if object!= None:
            serializer = UserSerializer(object, many=False)
            return Response({"message": "User is logged in", "User" : serializer.data})
        return Response({"message" : "user not found"}, status = 401)

class TaskViews:
    @api_view(['POST'])
    def CreateTask(request):
        user_object = User.objects.get(pk=request.data["id"])
        if user_object!=None:
            created_task = Task.objects.create(user=user_object,title = request.data["title"], description= request.data["description"])
            created_task = TaskSerializer(created_task, many=False)
            return Response({"message": "successfully saved", "Task" : created_task.data})
        return Response({"message" : "task not created"}, status = 401)
            
    @api_view(['GET'])
    def GetTasks(request):
        allTasks = Task.objects.all()
        serializer = TaskSerializer(allTasks, many=True)
        return Response(serializer.data)
    

    @api_view(['GET'])
    def TaskDetail(request, pk):
        try:
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(task, many=False)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

   
     
    @api_view(['DELETE'])
    def DeleteTask(request, pk):
        try:
            task_to_delete = Task.objects.get(id=pk)
            task_to_delete.delete()
            return Response({"message": "Task successfully deleted"})
        except Task.DoesNotExist:
            return Response({"Task not found"}, status=404) 
        

    @api_view(['POST'])
    def UpdateTask(request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({"message": "Task not found"}, status=404)

        task_serializer = TaskSerializer(task, data=request.data)

        if task_serializer.is_valid():
            task_serializer.save()
            return Response({"message": "Task successfully updated", "task": task_serializer.data})
        return Response({"message": "Invalid data provided for task update"}, status=400)
        




