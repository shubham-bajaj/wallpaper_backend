from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import ImageView,CategoryListView
router = routers.DefaultRouter()
router.register('api',ImageView)
router.register('category',CategoryListView)

urlpatterns = [
    path('',include(router.urls)),
]