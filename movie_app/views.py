from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .serialazers import *
from .models import *


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def test(request):
    if request.method == 'GET':
        directors_list = Director.objects.filter(user=request.user)
        serialazer = DirectorSerialazers(directors_list, many=True)
        return Response(data=serialazer.data)
    else:
        serializer = MovieValidateSerialazer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        title = serializer.validated_data['title']
        description = serializer.validated_data['description']
        duration = serializer.validated_data['duration']
        director = serializer.validated_data['director']
        user_id = serializer.validated_data['user_id']
        review = serializer.validated_data['review']
        movie = Movie.objects.create(title=title, description=description, director=director, duration=duration,
                                     user_id=user_id)
        movie.reviews_list.set(review)
        movie.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={
                            'message': 'movie created successfully',
                            'movie': MovieSerialazers(movie).data
                        })


@api_view(['GET', 'PUT', 'DELETE'])
def director(request, id):
    try:
        director_one = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={"message": 'Director not found'})
    if request.method == 'GET':
        serializer = DirectorSerialazers(director_one)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie_list_view.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        title = request.data.get('title', '')
        description = request.data.get('title', '')
        duration = request.data.get('duration ', '')
        director = request.data.get('director', '')
        user_id = request.data.get('user_id', None)
        review = request.data.get('review', [])
        movie.save()
        movie.reviews_list.set(review)
        movie.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={
                            'message': 'movie created successfully',
                            'movie': MovieSerialazers(movie).data
                        })


@api_view(['GET'])
def movie_list_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerialazers(movies, many=True).data
        return Response(data=data)


@api_view(['GET'], ['DELETE'], ['PUT'])
def movie(request, id):
    try:
        movie_one = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={"message": 'Movie not found'})
    if request.method == 'GET':
        serializer = MovieSerialazers(movie_one)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie_list_view.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = MovieValidateSerialazer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title = request.data.get('title', '')
        description = request.data.get('title', '')
        duration = request.data.get('duration ', '')
        director = request.data.get('director', '')
        user_id = request.data.get('user_id', None)
        review = request.data.get('review', [])
        movie.save()
        movie.reviews_list.set(review)
        movie.save()
        return Response(data=MovieValidateSerialazer(movie).data)


@api_view(['GET'])
def review_list_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerialazers(reviews, many=True).data
        return Response(data=data)
    else:
        serializer = MovieValidateSerialazer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        text = serializer.validated_data['text']
        movie_list = serializer.validated_data['movie_list']
        movie.reviews_list.set(review)
        movie.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={
                            'message': 'movie created successfully',
                            'movie': MovieSerialazers(movie).data
                        })


@api_view(['GET'])
def review(request, id):
    try:
        review_one = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={"message": 'Review not found'})
    serializer = ReviewSerialazers(review_one)
    return Response(data=serializer.data)
    if request.method == 'GET':
        serializer = MovieSerialazers(review_one)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review_list_view.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = MovieValidateSerialazer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title = request.data.get('title', '')
        movie_list = request.data.get('movie_list', '')
        stars = request.data.get('stars')
        review.save()
        review.reviews_list.set(review)
        reviewreview.save()
        return Response(data=MovieValidateSerialazer(review).data)


def validate_title(self, title):
    movies = Movie.objects.filter(title=title)
    if movies.count() > 0:
        raise ValidationError('Movie with this name already exists!')


@api_view(['GET'])
def directors_views(request):
    return Response()
