from rest_framework import serializers
from .models import *


class Studernt_deserialize_data(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    stu_id = serializers.IntegerField()
    place = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)