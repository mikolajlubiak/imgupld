from rest_framework import generics
from .models import Image, ImageTier
from .serializers import ImageSerializer, ImageTierSerializer
from .permissions import IsOwnerOrAdmin

class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ImageDetail(generics.RetrieveDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsOwnerOrAdmin]

class ImageTierList(generics.ListCreateAPIView):
    queryset = ImageTier.objects.all()
    serializer_class = ImageTierSerializer

class ImageTierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageTier.objects.all()
    serializer_class = ImageTierSerializer
