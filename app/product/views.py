from django.shortcuts import redirect, render
from rest_framework import viewsets, status
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


def index(request):
    return render(template_name='product/index.html', request=request)
