from django.shortcuts import render
from django.http import JsonResponse
from students.models import *
from  .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
# Manual serialization
# def studentsView(request):
#     students= Students.objects.all()
#     students_list=list(students.values())   
#     return JsonResponse(students_list,safe=False)


# Using Serializers
@api_view(['GET'])
def studentsView(request):
    if request.method=='GET':
        # GET ALL THE DATA FROM STUDENTS TABLE
        students=Students.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)