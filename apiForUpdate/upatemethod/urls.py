from django.urls import path, include
from upatemethod.views import update_product
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'products', ProductViewSet)
# router.register(r'products/<int:id>/', update_product, basename='update_products')

urlpatterns = [
    # path('', include(router.urls)),
    path(r'products/<int:pk>/', update_product)
]