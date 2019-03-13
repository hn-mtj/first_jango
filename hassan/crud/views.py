from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from crud.models import Crud
from crud.serializers import CrudSerializer
from rest_framework.throttling import UserRateThrottle


@csrf_exempt
def crud_list(request):
    """
    List all code crud, or create a new crud.
    """
    if request.method == 'GET':
        crud = Crud.objects.all()
        serializer = CrudSerializer(crud, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CrudSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def crud_detail(request, pk):
    """
    Retrieve, update or delete a code crud.
    """
    try:
        crud = Crud.objects.get(pk=pk)
    except Crud.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CrudSerializer(crud)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CrudSerializer(crud, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        crud.delete()
        return HttpResponse(status=204)