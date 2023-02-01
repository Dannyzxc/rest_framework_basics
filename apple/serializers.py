from rest_framework import serializers


class Studernt_serialize_data(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    stu_id = serializers.IntegerField()
    place = serializers.CharField(max_length=50)

