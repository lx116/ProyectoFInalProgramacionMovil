from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

from .models import Product
# Create your views here.


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': 'products-list/',
        'Detail': 'detail-view/<str:pk>/',
        'Create': 'create-product/',
        'Update': 'update-product/<str:pk>/',
        'Delete': 'delete_product/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def detail_products(request):
    pass


@api_view(['GET', 'POST', 'PUT'])
def shopping_cart(request):
    pass


@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_detail_product(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_new_product(request):
    print(request.data)

    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


