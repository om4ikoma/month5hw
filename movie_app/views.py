from .serialazers import *
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


class MovieModelViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerialazers
    lookup_field = 'id'


class MovieListCreatefAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerialazers


class MovieItemUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerialazers
    lookup_field = 'id'


class DirectorModelViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerialazers
    lookup_field = 'id'


class DirectorListCreatefAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerialazers


class DirectorItemUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerialazers
    lookup_field = 'id'


class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialazers
    lookup_field = 'id'


class ReviewListCreatefAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialazers


class ReviewtemUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialazers
    lookup_field = 'id'

