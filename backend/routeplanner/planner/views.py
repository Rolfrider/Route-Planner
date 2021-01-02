from django.http import HttpResponse, JsonResponse
from .serializers import NodeSerializer
from rest_framework.parsers import JSONParser
from .domain.router import route_for
# Create your views here.

def index(request):
    data = JSONParser().parse(request)
    serializer = NodeSerializer(data=data, many=True)
    if serializer.is_valid():
        places = []
        for place in serializer.data:
            places += [(place["lat"], place["lng"])]
        route = route_for(places)
        return JsonResponse(route, status=200, safe=False)
    return JsonResponse(serializer.errors, status=400)