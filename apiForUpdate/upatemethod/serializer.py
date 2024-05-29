from rest_framework import serializers
from upatemethod.models import Products


class ProductSerializer(serializers.ModelSerializer):
    product_id: int = serializers.IntegerField()
    class Meta:
        model = Products
        fields = "__all__"
        extra_kwargs = {
            'product_id':{'write_only':True}
        }
    
    def update(self, instance, valiadated_data):
        instance.product_id = valiadated_data.get('product_id', instance.product_id)
        instance.name = valiadated_data.get('name', instance.name)
        instance.category = valiadated_data.get('category', instance.category)
        instance.price = valiadated_data.get('price', instance.price)
        instance.save()
        return instance