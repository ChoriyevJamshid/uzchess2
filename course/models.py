from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

from utils.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Course(BaseModel):

    class Level(models.TextChoices):
        BEGINNER = 'BEG', 'Boshlang\'ch'
        AMATEUR = 'AMA', 'Havaskor'
        PROFESSIONAL = 'PRO', 'Professional'
        __empty__ = ''

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='courses')

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    level = models.CharField(max_length=3, choices=Level.choices,
                             default=Level.__empty__)

    price = models.DecimalField(max_digits=10, decimal_places=2,
                                default=0)
    price_discount = models.DecimalField(max_digits=10, decimal_places=2,
                                         blank=True, null=True)

    likes = models.ManyToManyField(get_user_model(), blank=True,
                                   related_name='like_courses')
    rating = models.PositiveSmallIntegerField(default=0, editable=False)

    buyers = models.ManyToManyField(get_user_model(), blank=True,
                                    related_name='buy_courses')
    cert_users = models.ManyToManyField(get_user_model(), blank=True,
                                        related_name='certificated_courses')

    def __str__(self):
        return self.title


class Chapter(BaseModel):

    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='chapters')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'course')


class Lesson(BaseModel):

    title = models.CharField(max_length=255)
    content = models.TextField()
    video = models.FileField(upload_to='videos/',
                             validators=[FileExtensionValidator(['mp4', 'avi'])])

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE,
                                related_name='lessons')
    finished_users = models.ManyToManyField(get_user_model(), blank=True,
                                            related_name='finished_lessons')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'chapter')


class Comment(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name='comments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='comments')
    content = models.CharField(max_length=500)

    rating = models.PositiveSmallIntegerField(default=0, editable=False)

    def __str__(self):
        return f'{self.course} {self.rating}'

