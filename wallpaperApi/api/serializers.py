from rest_framework import serializers
from .models import Image,CategoryList

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields='__all__'
        extra_kwargs = {
            'image': {'required': True},
            'publish':{'default':True},
        }
    
    image = serializers.ListField(child =serializers.ImageField())
    # Error: get method giving list of images that too null

class ImageGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields='__all__'
        extra_kwargs = {
            'image': {'required': True},
            'publish':{'default':True},
        }
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryList
        fields='__all__'
        