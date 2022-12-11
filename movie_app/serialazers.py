from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserSirealazers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id username first_name last_name'


class DirectorSerialazers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ReviewSerialazers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerialazers(serializers.ModelSerializer):
    user = UserSirealazers()
    reviews = ReviewSerialazers()
    reviews_list = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title description duration user director reviews'.split()


class MovieValidateSerialazer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(min_length=3, max_length=100)
    duration = serializers.CharField()
    user = serializers.IntegerField()

    def validate_user_id(self, user_id):
        try:
            User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValidationError('User does not exist')
        return user_id
