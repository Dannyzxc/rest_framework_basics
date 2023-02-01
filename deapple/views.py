from django.shortcuts import render, HttpResponse
from .models import *
from .serializers import *
import json
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    # check if request is post
    if request.method == 'POST':
        json_data = request.body
        # convert json data into stream
        stream = io.BytesIO(json_data)
        # convert stream data into python data
        python_data = JSONParser().parse(stream)
        # python data to complex data
        serialize_data = Studernt_deserialize_data(data=python_data)
        # if it is valid
        if serialize_data.is_valid():
            # then save the data
            serialize_data.save()
            res = {'massage': 'data created'}
            # then acknowledge
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serialize_data.errors)
        return HttpResponse(json_data, content_type='application/json')

