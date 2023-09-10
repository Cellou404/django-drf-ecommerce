from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class BrandViewSet(viewsets.ViewSet):
    """
    API endpoint that allows brands to be viewed or edited.
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductViewSet(viewsets.ViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
