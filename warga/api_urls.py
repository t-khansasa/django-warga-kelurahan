from django.urls import path, include
from .views import WargaListAPIView, WargaDetailAPIView, PengaduanListAPIView, WargaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')

urlpatterns = [
    # path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    # path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='api-warga-detail'),
    path('aduan/', PengaduanListAPIView.as_view(), name='api-pengaduan-list'),
    path('', include(router.urls)),
]