from django.urls import path
from .views import delete_products

urlpatterns = [
    path(r'delprod/<int:pk>/', delete_products)
]