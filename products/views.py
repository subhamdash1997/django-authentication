from django.shortcuts import render
from .models import Product
from .serializer import ProductSerializer,MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .test import Message

from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics




# GENERIC VIEWS

class ListProductGenerics(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class DetailedProductGenerics(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    





















# MIXIN VIEWS


# class ListProductMixins(mixins.ListModelMixin,generics.GenericAPIView):
    
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# class DetailedProductMixins(mixins.RetrieveModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
    
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)



# CLASS BASED VIEWS


# class Products(APIView):
#     def get(self,request):
#         query = Product.objects.all()
#         serializer = ProductSerializer(query,many=True)
#         return Response({'status':200,'data':serializer.data})
        

# class ProductDetailView(APIView):
#     def get(self,request,pid):
#         query = Product.objects.filter(product_id=pid)
#         serializer = ProductSerializer(query,many=True)
#         return Response({'status':200,'data':serializer.data})



# FUNCTION BASED VIEWS

# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
# def list_products(request):
#     query = Product.objects.all()
#     serializers_class = ProductSerializer(query,many=True)
#     return Response({'status':200,'serializers_class_data':serializers_class.data})


# @api_view(['GET','POST'])
# def list_messages(request):
#     query = Message('subham.webdev1997@gmail.com', 'This is test content.')
#     serializer = MessageSerializer(query)
#     return Response({'status': 201, 'serializer_class_data': serializer.data})
