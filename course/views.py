from django.db import models as db_models
from django.db.models import functions
from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from course import models
from course import serializers as ser


class CourseListAPIView(generics.ListAPIView):
    queryset = models.Course.objects.all()
    serializer_class = ser.CourseSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        courses = super().get_queryset().select_related(
            "category"
        )
        courses = courses.annotate(
            chapters_count=db_models.Count('chapters'),
            is_like=functions.Coalesce(db_models.Exists(
                self.request.user.like_courses.filter(id=db_models.OuterRef('id'))
            ), False)
        )

        if self.request.query_params:
            courses = courses.filter(title__startswith=self.request.query_params['title'])
        return courses


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Course.objects.all()
    serializer_class = ser.CourseDetailSerializer


class ChapterDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ser.ChapterDetailSerializer

    def get_queryset(self):
        return super().get_queryset().filter(
            course_id=self.kwargs.get('course_id')
        )






