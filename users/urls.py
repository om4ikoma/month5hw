from django.urls import path
from users import views

urlpatterns = [
    path('registration/', views.RegisterAPIView.as_view()),
    path('authorization/', views.LoginAPIView.as_view()),
]