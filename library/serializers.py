from rest_framework import serializers
from library.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'price', 'discount_price', 'image', 'level', 'author',
                  'pages_count', 'published_at', 'description')

