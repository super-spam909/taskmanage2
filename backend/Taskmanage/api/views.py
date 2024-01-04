from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework.decorators import api_view


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
        


