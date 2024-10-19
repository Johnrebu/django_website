from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Student
from .serialize import UserSerializer


# Create your views here.

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_request(request):
    students=Student.objects.all()
    user=UserSerializer(students,many=True)
    return Response(user.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def post_request(request):
    create=UserSerializer(data=request.data)
    if create.is_valid():
        create.save()
        return Response(create.data,status=status.HTTP_201_CREATED)
    else:
        return Response(create.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_request(request,id):
    user=Student.objects.get(id=id)
    update=UserSerializer(user,data=request.data)
    if update.is_valid():
        update.save()
        return Response(update.data,status=status.HTTP_200_OK)
    else:
        return Response(update.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_request(request,id):
    user = Student.objects.get(id=id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




















