from rest_framework import serializers
from productApi.models import Products


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    product_id: int = serializers.ReadOnlyField()
    class Meta:
        model = Products
        fields = "__all__"

        def update(self, instance, valiadated_data):
            instance.product_id = valiadated_data.get('product_id', instance.product_id)
            instance.name = valiadated_data.get('name', instance.name)
            instance.category = valiadated_data.get('category', instance.category)
            instance.price = valiadated_data.get('price', instance.price)
            instance.save()
            return instance