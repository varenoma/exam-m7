from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import JournalViewSet, AllJournalListAndDetail


router = DefaultRouter()
router.register(r'only-author', JournalViewSet, basename="only_authors")
router.register(r'all_verified_journals', AllJournalListAndDetail,
                basename='all-verified-journals')


urlpatterns = [
    path('', include(router.urls))
]
