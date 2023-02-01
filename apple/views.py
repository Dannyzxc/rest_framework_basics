from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
import json


# Create your views here.
def home(request):
    # imported data
    stud = Student.objects.get(id=2)
    # converting complex data to python (dictionary) data
    serialize_data = Studernt_serialize_data(stud)
    # converting python data to json data
    json_data = JSONRenderer().render(serialize_data.data)
    # mention the type of data sending
    return HttpResponse(json_data,content_type='application/json')

def select(request,pk):
    # imported data
    stud = Student.objects.get(id=pk)
    # converting complex data to python (dictionary) data
    serialize_data = Studernt_serialize_data(stud)
    # converting python data to json data
    json_data = JSONRenderer().render(serialize_data.data)
    # mention the type of data sending
    return HttpResponse(json_data,content_type='application/json')


def student_list(request):
    # imported data
    stud = Student.objects.all()
    # converting complex data to python (dictionary) data and for many
    serialize_data = Studernt_serialize_data(stud,many=True)
    # converting python data to json data
    json_data = JSONRenderer().render(serialize_data.data)
    # mention the type of data sending
    return HttpResponse(json_data,content_type='application/json')


# another way to send data with less line of code
def student_list_json(request):
    # imported data
    stud = Student.objects.all()
    print(type(stud))
    # converting complex data to python (dictionary) data and for many
    serialize_data = Studernt_serialize_data(stud,many=True)
    print(type(serialize_data))
    print(type(serialize_data.data))
    # converting python data to json data in list and sending it ( default 'safe=True')
    return JsonResponse(serialize_data.data,safe=False)
