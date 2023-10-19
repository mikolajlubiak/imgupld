from django.urls import path
from .views import ImageList, ImageDetail, ImageTierList, ImageTierDetail

urlpatterns = [
    path('images/', ImageList.as_view(), name='image-list'),
    path('images/<int:pk>/', ImageDetail.as_view(), name='image-detail'),
    path('tiers/', ImageTierList.as_view(), name='tier-list'),
    path('tiers/<int:pk>/', ImageTierDetail.as_view(), name='tier-detail'),
]
