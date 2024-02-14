from rest_framework import serializers
from library.models import Book, CartItem


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'price', 'discount_price', 'image', 'level', 'author',
                  'pages_count', 'published_at', 'description')


class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'book', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.quantity * obj.book.price

    def create(self, validated_data):
        cart = validated_data.pop('cart')
        book = validated_data.pop('book')
        quantity = validated_data.pop('quantity', 1)
        cart_item, _ = CartItem.objects.get_or_create(cart=cart, book=book)
        cart_item.quantity += quantity
        cart_item.save()
        return cart_item
