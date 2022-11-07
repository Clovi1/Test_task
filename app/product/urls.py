from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('product', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', views.index),
    path('', include(router.urls)),
]
