from .serializers import NodeSerializer

def validate_planner(request):
    res = {}
    res["success"] = True
    res["errors"] = None
    res["details"] = None
    validation = NodeSerializer(data=request, many=True)
    if validation.is_valid():
        res["success"] = True
    else:
        res["success"] = False
        res["details"] = "Bad Request Body"
        res["errors"] = validation.errors
    return res