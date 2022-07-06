from rest_framework import serializers
from products.models import Product, Warehouse


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['name', 'address']

class ProductSerializer(serializers.ModelSerializer):
    warehouses = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['title', 'created', 'warehouses']

    def get_warehouses(self, obj):
        warehouses = obj.warehouse.all()
        serializer = WarehouseSerializer(warehouses, many=True)

        return serializer.data

