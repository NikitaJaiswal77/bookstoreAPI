from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Book
from .serializers import BookSerializer
from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], 
            password=validated_data['password']
        )
        return user


class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['title', 'author', 'isbn']
    ordering_fields = ['price']
    def list(self, request, *args, **kwargs):
        # Get the list of books from the queryset
        queryset = self.get_queryset() 
        serializer = self.get_serializer(queryset, many=True)

       
        return Response({
            "message": "Books retrieved successfully!",  
            "books": serializer.data  
        }, status=status.HTTP_200_OK)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Apply price filtering
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)  
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)  
        
        return queryset

  

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the book object
        serializer = self.get_serializer(instance)  # Serialize the book object
        return Response({
            "message": f"Book '{instance.title}' retrieved successfully!", 
            "book": serializer.data  # Return the specific book data
        }, status=status.HTTP_200_OK)

   
    def update(self, request, *args, **kwargs):
        instance = self.get_object() 
        serializer = self.get_serializer(instance, data=request.data, partial=True) 

        if serializer.is_valid():  
            updated_book = serializer.save()  
            return Response({
                "message": f"Book '{updated_book.title}' by {updated_book.author} updated successfully!",  
                "book": BookSerializer(updated_book).data  
            }, status=status.HTTP_200_OK)

        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  
        title = instance.title
        author = instance.author
        self.perform_destroy(instance)
        return Response({
            "message": f"Book '{title}' by {author} deleted successfully!"  
        }, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete() 