from rest_framework import serializers

from .models import Item, Review, Vendor, Category


class FilterReviewListSerializer(serializers.ListSerializer):
    """"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)
    

class RecursiveSerializer(serializers.Serializer):
    """"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data
    

class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""
    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзыва"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ("name", "text", "children")


class VendorListSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Vendor
        fields = ("title", "url")


class VendorDetailSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Vendor
        fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Category
        fields = ("name", "url")


class CategoryDetailSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Category
        fields = "__all__"


class ItemListSerializer(serializers.ModelSerializer):
    """Список товаров"""
    class Meta:
        model = Item
        fields = ("title", "description", "amount", "price")

        
class ItemDetailSerializer(serializers.ModelSerializer):
    """Описание товара"""
    category = CategoryDetailSerializer(read_only=True)
    vendor = VendorDetailSerializer(read_only=True)
    reviews = ReviewCreateSerializer(many=True)

    class Meta:
        model = Item
        exclude = ("url",)
