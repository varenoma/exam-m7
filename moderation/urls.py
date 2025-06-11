from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ModerationViewSet

router = DefaultRouter()
router.register(r'moder', ModerationViewSet, basename='moder')

urlpatterns = [
    path('', include(router.urls))
]
