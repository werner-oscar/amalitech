from rest_framework import serializers


class DetectFaceSerializer(serializers.Serializer):
    image = serializers.ImageField(required = True)