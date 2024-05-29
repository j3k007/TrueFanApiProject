from rest_framework import status
from rest_framework.decorators import api_view
from upatemethod.models import Products
from upatemethod.serializer import ProductSerializer
from rest_framework.response import Response


# Create your views here.

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer

@api_view(['PUT'])
def update_product(request, pk):
    serializer_context = {
        'request':request,
    }
    try:
        products = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(products, data=request.data, context=serializer_context)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)