from rest_framework import serializers
from .models import *


class Studernt_serialize_data(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    stu_id = serializers.IntegerField()
    place = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.stu_id = validated_data.get('stu_id',instance.stu_id)
    #     instance.place = validated_data.get('place',instance.place)
 