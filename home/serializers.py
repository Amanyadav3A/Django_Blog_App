from rest_framework import serializers
from .models import input_post

class post_serializer(serializers.ModelSerializer):
    class Meta:
        model = input_post
        fields = "__all__"