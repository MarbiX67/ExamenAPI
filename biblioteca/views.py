from rest_framework import viewsets, permissions
from .models import Autor, Libro, Prestamo
from .serializers import AutorSerializer, LibroSerializer, PrestamoSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all().order_by('id')
    serializer_class = AutorSerializer
    permission_classes = [permissions.IsAuthenticated]  #

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all().order_by('id')
    serializer_class = LibroSerializer
    permission_classes = [permissions.IsAuthenticated]

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all().order_by('id')
    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAuthenticated]