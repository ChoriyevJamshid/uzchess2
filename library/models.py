from django.db import models
from utils.models import BaseModel


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

    image = models.ImageField(upload_to='books')
    level = models.CharField(max_length=16, choices=Level.choices, default=Level.AMATEUR)
    author = models.CharField(max_length=64)
    pages_count = models.PositiveIntegerField(default=0)
    published_at = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title




