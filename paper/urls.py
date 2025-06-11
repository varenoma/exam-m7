from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllPaperListAndDetail, PaperViewSet

router = DefaultRouter()
router.register(r'only-author', PaperViewSet, basename='only_authors')
router.register(r'all_verified_papers',
                AllPaperListAndDetail, basename='all_verified_papers')

urlpatterns = [
    path('', include(router.urls)),
]
