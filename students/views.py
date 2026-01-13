from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def students(request):
    students = [
        {
            'id': 1,
            'name': 'John',
            'age': 25,
            'city': 'New York'
        },
        {
            'id': 2,
            'name': 'Jane',
            'age': 30,
            'city': 'Los Angeles'
        },
        {
            'id': 3,
            'name': 'Bob',
            'age': 35,
            'city': 'Chicago'
        }
    ]
    return HttpResponse(students)