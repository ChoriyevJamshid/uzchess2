from rest_framework import serializers as s

from course import models


class CourseSerializer(s.ModelSerializer):
    category = s.StringRelatedField(source="category.title")
    chapters_count = s.IntegerField()
    is_like = s.BooleanField()

    class Meta:
        model = models.Course
        fields = ('title', 'author', 'price_discount', 'price', 'level',
                  'category', 'chapters_count', 'is_like')


class ChapterSerializer(s.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = '__all__'


class LessonSerializer(s.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = '__all__'


class CommentSerializer(s.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'

