from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import generics
from .serializers import ProductSerializer
from cart.models import Product


class UserAPI(APIView):
    def post(self, request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            user = serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    