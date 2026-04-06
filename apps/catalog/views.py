from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from django_filters.rest_framework import  DjangoFilterBackend
from .serializers import ProductCategorySerializer, ProductSerializer
from .models.product import Product
from .models.product_category import ProductCategory



class ProductView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'price',]

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)






class ProductCategoryView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


    def get_object(self, pk):
        try:
            return ProductCategory.objects.get(id=pk)
        except ProductCategory.DoesNotExist:
            raise NotFound('Category is not found.')

    def get(self, request, pk=None):
        if pk:
            ctg = self.get_object(pk)
            serializer = self.get_serializer(ctg)
        else:
            ctgs = ProductCategory.objects.all()
            serializer = self.get_serializer(ctgs, many=True)

        return Response(serializer.data, status=200)