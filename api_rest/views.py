from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serialize import UserSerializer

import json


# Create your views here.

@api_view(['GET'])
def get_user(request):
    if request.method == "GET":
        user = User.objects.all() # Query all users
        serialize = UserSerializer(user, many=True) # Serialize the data

        return Response(serialize.data) # Return the data
    
    return Response(status=status.HTTP_400_BAD_REQUEST) # Return a bad request status


@api_view(["GET"])
def get_user_by_name(request, name):
    try:
        user = User.objects.get(pk=name) # Query the user by name
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serialize = UserSerializer(user)
        return Response(serialize.data)
    


# Create a new user
@api_view(["POST"])
def create_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        serialize = UserSerializer(data=data)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Update a user
@api_view(["PUT"])
def update_user(request, name):
    try:
        user = User.objects.get(pk=name)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        data = json.loads(request.body)
        serialize = UserSerializer(user, data=data)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
        
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)