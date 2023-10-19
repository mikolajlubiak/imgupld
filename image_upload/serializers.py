from rest_framework import serializers
from .models import Image, ImageTier

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ImageTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTier
        fields = '__all__'
