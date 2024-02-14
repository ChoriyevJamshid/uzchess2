from django.urls import path
from library import views

urlpatterns = [
    path('', views.BookListAPIView.as_view())
]
