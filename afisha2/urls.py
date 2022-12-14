"""afisha2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movie_app import views
from . import swagger
LIST_CREATE = {
    'get': 'list', 'post': 'create'
}
ITEM_UPDATE_DELETE = {
    'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movie_CBV', views.MovieListCreatefAPIView.as_view()),
    path('api/v1/movie_CBV/<int:id>', views.MovieItemUpdateDeleteAPIView.as_view()),
    path('api/v1/movie_CBV', views.ModelViewSet.as_view(LIST_CREATE)),
    path('api/v1/movie_CBV/<int:id>', views.ModelViewSet.as_view(ITEM_UPDATE_DELETE)),
    path('api/v1/director_CBV', views.DirectorListCreatefAPIView.as_view()),
    path('api/v1/director_CBV/<int:id>', views.DirectorItemUpdateDeleteAPIView.as_view()),
    path('api/v1/review_CBV', views.ReviewListCreatefAPIView.as_view()),
    path('api/v1/review_CBV/<int:id>', views.ModelViewSet.as_view(ITEM_UPDATE_DELETE)),
    path('api/v1/users', include('users/urls'))
]

urlpatterns += swagger.urlpatterns
