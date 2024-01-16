from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserSerializer, TaskSerializer
from .models import User, Task 
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
import jwt, datetime 
from django.conf import settings 

### for password recovery


# Create your views here.

class UserViews:
    @api_view(['POST'])
    def registerUser(request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'user' : serializer.data, 'message' : 'user created'}, status=201)
        
        return Response(serializer.errors, status=400)

    
    
    
    @api_view(['GET'])
    def getUsers(request):
        allUsers = User.objects.all()
        serializer = UserSerializer(allUsers, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    def whoamI(request):
        token= request.COOKIES.get('jwt')

        if not token:
             return Response({"message" : "unauthaorized"}, status = 401)
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms = ['HS256'])
        except jwt.ExpiredSignatureError:
             return Response({"message" : "unauthaorized"}, status = 401)
        
        user = User.objects.get(pk=payload['id'])
        serializer= UserSerializer(user, many=False)
        return Response(serializer.data)
            

        

    @api_view(['POST'])
    def login(request):
        object = User.objects.get(username=request.data["username"], password=request.data["password"])
        if object!= None:
    
            payload={'id': object.id, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60), 'iat' : datetime.datetime.utcnow()}
            token=jwt.encode(payload,settings.SECRET_KEY, algorithm= 'HS256')
            response= Response()
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data={"message": "User is logged in", 'jwt' : token}
            return response
        return Response({"message" : "user not found"}, status = 401)


    @api_view(['POST'])
    def logout(request):
        response = Response()
        response.delete_cookie('jwt')
        response.data={'message': "you have been logged out"}
        return response 

    
   
"""
    @api_view(['POST'])
    def resetPassword(request):
        email = request.data.get('email', '')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
                return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

            # Generate a password reset token
        token_generator = default_token_generator
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)

            # Include the reset link in the response (you can also send it via email)
        reset_link = f"http://your-frontend-url/reset-password/{uid}/{token}/"
        return Response({"message": "Password reset link sent", "reset_link": reset_link})
"""
        
class TaskViews:
    @api_view(['POST'])
    def CreateTask(request):
        token= request.COOKIES.get('jwt')

        if not token:
             return Response({"message" : "unauthaorized"}, status = 401)
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms = ['HS256'])
        except jwt.ExpiredSignatureError:
             return Response({"message" : "unauthaorized"}, status = 401)
        
        user = User.objects.get(pk=payload['id'])
        if user!=None:
            created_task = Task.objects.create(user=user,title = request.data["title"], description= request.data["description"])
            created_task = TaskSerializer(created_task, many=False)
            return Response({"message": "successfully saved", "Task" : created_task.data})
        return Response({"message" : "task not created"}, status = 401)
            
    @api_view(['GET'])
    def GetTasks(request):
        token= request.COOKIES.get('jwt')

        if not token:
             return Response({"message" : "unauthaorized"}, status = 401)
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms = ['HS256'])
        except jwt.ExpiredSignatureError:
             return Response({"message" : "unauthaorized"}, status = 401)
        
        user = User.objects.get(pk=payload['id'])
        allTasks = Task.objects.filter(user=user)
        serializer = TaskSerializer(allTasks, many=True)
        return Response(serializer.data)
    

    @api_view(['GET'])
    def TaskDetail(request, pk):
        token= request.COOKIES.get('jwt')

        if not token:
             return Response({"message" : "unauthaorized"}, status = 401)
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms = ['HS256'])
        except jwt.ExpiredSignatureError:
             return Response({"message" : "unauthaorized"}, status = 401)
        
        #user = User.objects.get(pk=payload['id'])
        try:
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(task, many=False)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

   
     
    @api_view(['POST'])
    def DeleteTask(request):
        token= request.COOKIES.get('jwt')

        if not token:
             return Response({"message" : "unauthaorized"}, status = 401)
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms = ['HS256'])
        except jwt.ExpiredSignatureError:
             return Response({"message" : "unauthaorized"}, status = 401)
        
        user = User.objects.get(pk=payload['id'])

        

        try:
            task_to_delete = Task.objects.get(pk=request.data['id'])

            if task_to_delete.user != user:
                 return Response({"message": "not authorized to access it "}, status=404)
            task_to_delete.delete()
            return Response({"message": "Task successfully deleted"})
        except Task.DoesNotExist:
            return Response({"Task not found"}, status=404) 
        

    @api_view(['POST'])
    def UpdateTask(request):
        token= request.COOKIES.get('jwt')

        if not token:
             return Response({"message" : "unauthaorized"}, status = 401)
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms = ['HS256'])
        except jwt.ExpiredSignatureError:
             return Response({"message" : "unauthaorized"}, status = 401)
        
        
        user = User.objects.get(pk=payload['id']) 


        
        try:
            task = Task.objects.get(pk=request.data['id'])
        
            if task.user != user:
                 return Response({"message": "not authorized to access it "}, status=404)



        except Task.DoesNotExist:
            return Response({"message": "Task not found"}, status=404)

        task_serializer = TaskSerializer(task, data=request.data)

        if task_serializer.is_valid():
            task_serializer.save()
            return Response({"message": "Task successfully updated", "task": task_serializer.data})
        return Response({"message": "Invalid data provided for task update"}, status=400)
        




