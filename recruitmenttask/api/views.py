from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from products.models import Product, Warehouse
from .serializers import ProductSerializer, WarehouseSerializer

@api_view(['GET'])
def getRouters(request):
    routes = [
        {'GET': '/api/products'},
        {'POST': 'api/products/create'},
        {'PUT': 'api/products/edit/title/'},
        {'GET': 'api/products/warehouses'}
    ]

    return Response(routes)


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postProduct(request):
    serializer = ProductSerializer(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def putProduct(request, pk):
    product = Product.objects.filter(title=pk).first()
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getWarehouse(request):
    warehouse = Warehouse.objects.all()
    serializer = WarehouseSerializer(warehouse, many=True)
    return Response(serializer.data)













