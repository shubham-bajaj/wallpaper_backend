from django.shortcuts import render
from .serializers import ImageSerializer,CategoryListSerializer,ImageGetSerializer
from .models import Image,CategoryList
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_queryset(self):
        self.serializer_class = ImageGetSerializer
        queryset = Image.objects.all()
        fname = self.request.query_params.get('fname')
        if fname=="hinduGod":
            return queryset
        if fname is not None:
            queryset = queryset.filter(fname=fname) 
        return queryset
    def create(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            images= serializer.validated_data['image']
            fname = serializer.validated_data['fname']
            # Save each image file to your media directory or to your database
            for image in images:
                img = Image(fname = fname,image =image) 
                img.save()
            
            return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class CategoryListView(viewsets.ModelViewSet):
    queryset = CategoryList.objects.all()
    serializer_class = CategoryListSerializer