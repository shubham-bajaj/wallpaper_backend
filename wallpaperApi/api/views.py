from django.shortcuts import render
from .serializers import ImageSerializer,CategoryListSerializer
from .models import Image,CategoryList
from rest_framework import viewsets
# Create your views here.

class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_queryset(self):
        queryset = Image.objects.all()
        fname = self.request.query_params.get('fname')
        if fname=="hinduGod":
            return queryset
        if fname is not None:
            queryset = queryset.filter(fname=fname) 
        return queryset


    
class CategoryListView(viewsets.ModelViewSet):
    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer