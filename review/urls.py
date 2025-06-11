from django.urls import include, path
from rest_framework.routers import DefaultRouter

from review.views import ReviewViewSet


router = DefaultRouter()
router.register(r'', ReviewViewSet, basename='review')


urlpatterns = [
    path('', include(router.urls))
]
