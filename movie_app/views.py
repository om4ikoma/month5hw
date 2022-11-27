from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialazers import DirectorSerialazers
from .models import *


@api_view(['GET'])
def test(request):
    directors_list = Director.objects.all()
    serialazer = DirectorSerialazers(directors_list, many=True)
    return Response(data=serialazer.data)


@api_view(['GET'])
def director(request, id):
    try:
        director_one = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'Director not find'})
        if request.method == 'GET':
            serializer = DirectorSerialazers(director_one)
        return Response(data=serializer.data)


@api_view(['GET'])
def directors_views(request):
    return Response()
