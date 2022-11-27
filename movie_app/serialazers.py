from rest_framework import serializers
from .models import *


class DirectorSerialazers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
