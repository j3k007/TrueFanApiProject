from django.urls import path, include
from productApi.views import ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('updateProd/<int:id>/', update_prod, name='updateProd')
]   