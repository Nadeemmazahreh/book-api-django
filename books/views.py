from rest_framework import generics
from .serializers import BookSerializer
from .models import Book


# Create your views here.
class BookList(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer