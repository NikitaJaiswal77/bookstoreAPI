from django.contrib import admin
from django.urls import path
from .views import   BookListCreate, BookDetail 


urlpatterns = [
    # operations
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    # path('api/register/', RegisterView.as_view(), name='register'),
]
