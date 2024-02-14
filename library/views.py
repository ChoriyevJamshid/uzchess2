from django.shortcuts import render
from rest_framework.generics import ListAPIView
from library.models import Book
from library.serializers import BookSerializer


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

