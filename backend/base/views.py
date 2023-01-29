from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
# from .products import products
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def getRouters(request):
  routes=[
    '/api/products/',
    '/api/products/create/',
    '/api/products/upload/',
    '/api/products/<id>/reviews/',
    '/api/products/top/',
    '/api/products/<id>/',
    '/api/products/delete/<id>/',
    '/api/products/update/<id>',
    ]
  return Response(routes)

@api_view(['GET'])
def getProducts(request):
  products=Product.objects.all()
  serialiser=ProductSerializer(products, many=True)
  return Response(serialiser.data)

@api_view(['GET'])
def getProduct(request,pk):
  product=Product.object.id(_id=pk)
  serializer=ProductSerializer(product, many=False)
  return Response(serializer.data)

