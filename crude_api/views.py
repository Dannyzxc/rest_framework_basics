from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def parse_data(request):
    if request.method == "GET":
        # try:
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stud = Student.objects.get(id=id)
            serializer_data = Studernt_serialize_data(stud)
            json_data = JSONRenderer().render(serializer_data.data)
            return HttpResponse(json_data, content_type='application/json')

        stud = Student.objects.all()
        print(stud)
        serializer_data = Studernt_serialize_data(stud, many=True)
        print(serializer_data)
        json_data = JSONRenderer().render(serializer_data.data)
        print(json_data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer_data = Studernt_serialize_data(data=python_data)
        if serializer_data.is_valid():
            serializer_data.save()
            response_data = {'msg':'data created'}
            json_data = JSONRenderer().render(response_data)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer_data.errors)
        return HttpResponse(json_data, content_type='application/json')


def home(request):
    return HttpResponse('hello world')
