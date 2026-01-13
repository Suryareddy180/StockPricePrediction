from django.shortcuts import render
from django.http import JsonResponse
from students.models import *
# Create your views here.
def studentsView(request):
    students= Students.objects.all()
    students_list=list(students.values()) 
    return JsonResponse(students_list,safe=False)
  