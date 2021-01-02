from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .mapprovider.map import get_graph
from .serializers import NodeSerializer
from rest_framework.parsers import JSONParser
import json
# Create your views here.

def index(request):
    data = JSONParser().parse(request)
    serializer = NodeSerializer(data=data, many=True)
    if serializer.is_valid():
        print(serializer.data)
        return JsonResponse(lol, status=200, safe=False)
    return JsonResponse(serializer.errors, status=400)