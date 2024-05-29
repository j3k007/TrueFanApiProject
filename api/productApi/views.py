from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from productApi.models import Products
from productApi.serializer import ProductSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, pk=None):
        response = {'massage':'Delete function is not allowed.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)