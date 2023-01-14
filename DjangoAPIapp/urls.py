from django.urls import path, include
from rest_framework.routers import DefaultRouter
from DjangoAPIapp import views


urlpatterns=[
    path('', views.api_root),
    path('category/', views.CategoryList.as_view(), name="category-list"),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name="category-detail"),
    path('product/', views.ProductList.as_view(), name="product-list"),
    path('product/<int:pk>', views.ProductDetail.as_view(), name="product-detail"),
    path('book/', views.BookList.as_view(),name="book-list"),
    path('book/<int:pk>', views.BookDetail.as_view(), name="book-detail"),
]
