from django.urls import path

from course import views

urlpatterns = [
    path('', views.CourseListAPIView.as_view()),
    path('<int:pk>/', views.CourseDetailAPIView.as_view()),
    path('<int:course_id>/<int:pk>/', views.ChapterDetailAPIView.as_view())

]

