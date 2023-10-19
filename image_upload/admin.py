from django.contrib import admin
from .models import Image, ImageTier

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'uploaded_at')
    list_filter = ('user',)

@admin.register(ImageTier)
class ImageTierAdmin(admin.ModelAdmin):
    list_display = ('name', 'original_link', 'expiring_link')
