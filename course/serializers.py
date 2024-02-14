from django.contrib.auth import get_user_model
from django.db.models.functions import Coalesce
from rest_framework import serializers as s
from django.db.models import Count, Exists, OuterRef

from course import models


class LessonSerializer(s.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = ('title', 'video')


class ChapterSerializer(s.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = models.Chapter
        fields = ('title', 'lessons')


class CommentSerializer(s.ModelSerializer):
    user = s.StringRelatedField(source="user.username")

    class Meta:
        model = models.Comment
        fields = ('user', 'content', 'created_at', 'rating')


class CourseSerializer(s.ModelSerializer):
    category = s.StringRelatedField(source="category.title")
    chapters_count = s.IntegerField()
    is_like = s.BooleanField()

    class Meta:
        model = models.Course
        fields = ('title', 'author', 'price_discount', 'price', 'level',
                  'category', 'chapters_count', 'is_like')


class CourseDetailSerializer(s.ModelSerializer):
    chapters_count = s.SerializerMethodField()
    lessons_count = s.SerializerMethodField()
    is_like = s.SerializerMethodField()
    chapters = ChapterSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = models.Course
        fields = ('title', 'level', 'price', 'price_discount', 'rating',
                  'chapters_count', 'lessons_count', 'is_like', 'chapters', 'comments')

    def get_lessons_count(self, obj):
        return obj.chapters.aggregate(lessons_count=Count('lessons'))['lessons_count']

    def get_chapters_count(self, obj):
        return obj.chapters.count()

    def get_is_like(self, obj):
        return True if self.context['request'].user in obj.likes.all() else False


class LessonDetailSerializer(s.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = ('video', 'content')


class ChapterDetailSerializer(s.ModelSerializer):
    lessons = LessonDetailSerializer(many=True)
    lessons_list = s.SerializerMethodField()

    class Meta:
        model = models.Chapter
        fields = ('title', 'lessons', 'lessons_list')

    def get_lessons_list(self, obj):
        lessons = obj.lessons.annotate(
            is_view=Coalesce(
                Exists(self.context['request'].user.finished_lessons.filter(
                    id=OuterRef('id'))
                ), False
            )
        ).values_list('title', 'is_view')

        return lessons




