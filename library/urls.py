from django.urls import path
from library import views
from .views import AddToCartView, ViewCartView


urlpatterns = [
    path('', views.BookListAPIView.as_view()),
    path('detail/<int:pk>/', views.BookRetrieveAPIView.as_view()),
    path('add-to-cart/<int:book_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', ViewCartView.as_view(), name='cart'),

]
