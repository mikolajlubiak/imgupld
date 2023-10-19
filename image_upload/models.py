from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.CharField(max_length=20, choices=[("Basic", "Basic"), ("Premium", "Premium"), ("Enterprise", "Enterprise")])

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ImageTier(models.Model):
    name = models.CharField(max_length=50)
    thumbnail_sizes = models.TextField()
    original_link = models.BooleanField(default=False)
    expiring_link = models.BooleanField(default=False)
