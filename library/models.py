from django.db import models
from utils.models import BaseModel
from django.contrib.auth import get_user_model


class Level(models.TextChoices):
    BEGINNER = 'BEG', 'Boshlang\'ch'
    AMATEUR = 'AMA', 'Havaskor'
    PROFESSIONAL = 'PRO', 'Professional'


class Category(BaseModel):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Book(BaseModel):
    title = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='books')
    level = models.CharField(max_length=16, choices=Level.choices, default=Level.AMATEUR)
    author = models.CharField(max_length=64)
    pages_count = models.PositiveIntegerField(default=0)
    published_at = models.DateField()
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    items = models.ManyToManyField('Book', through='CartItem')

    def __str__(self):
        return f"Cart for {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='cartitems')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.book.title} in {self.cart}"


