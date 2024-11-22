from django.contrib import admin
from django.urls import path
from .views import   BookListCreate, BookDetail 
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # operations
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    # path('api/register/', RegisterView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

