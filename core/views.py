from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # [IsAuthenticated]
