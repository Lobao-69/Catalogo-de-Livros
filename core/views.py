from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSetRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer