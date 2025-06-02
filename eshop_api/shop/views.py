from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import Item, Vendor, Category
from .serializers import ItemListSerializer, ItemDetailSerializer, ReviewCreateSerializer, VendorListSerializer, VendorDetailSerializer, CategoryDetailSerializer, CategoryListSerializer
#from .service import ItemFilter


class ItemListView(generics.ListAPIView):
    """Вывод списка товаров"""
    serializer_class = ItemListSerializer
    #filter_backends = (DjangoFilterBackend, )
    #filterset_class = ItemFilter
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        items = Item.objects.all()
        return items
    

class ItemDetailView(generics.RetrieveAPIView):
    """Вывод описания товара"""
    queryset = Item.objects.filter()
    serializer_class = ItemDetailSerializer


class ReviewCreateView(generics.CreateAPIView):
    """Добавление отзыва к товару"""
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class VendorsListView(generics.ListAPIView):
    """Вывод списка брендов"""
    queryset = Vendor.objects.all()
    serializer_class = VendorListSerializer


class VendorsDetailView(generics.RetrieveAPIView):
    """Вывод описания бренда"""
    queryset = Vendor.objects.all()
    serializer_class = VendorDetailSerializer


class CategoriesListView(generics.ListAPIView):
    """Вывод списка брендов"""
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoriesDetailView(generics.RetrieveAPIView):
    """Вывод описания бренда"""
    lookup_field = "url"
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
