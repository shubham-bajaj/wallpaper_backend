from rest_framework import serializers
from .models import Image,CategoryList

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields='__all__'
        extra_kwargs = {
            'image': {'required': True},
        }
    # image = serializers.ListField(child =serializers.ImageField())

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryList
        fields='__all__'
        