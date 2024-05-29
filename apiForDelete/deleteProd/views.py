from rest_framework import status
from rest_framework.decorators import api_view
from deleteProd.models import Products
from deleteProd.serializer import ProductSerializer
from rest_framework.response import Response

# Create your views here.


@api_view(['DELETE'])
def delete_products(request, pk):
    try:
        products = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    products.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
