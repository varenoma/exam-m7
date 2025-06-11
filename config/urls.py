from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from config import settings


schema_view = get_schema_view(
    openapi.Info(
        title="Exam 7",
        default_version='v1',
        description="N62 Mamadaliyev Shukurullo",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="varenoma@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/account/', include('account.urls')),
    path('api/contact/', include('contact.urls')),
    path('api/infos/', include('info.urls')),
    path('api/journal/', include('journal.urls')),
    path('api/paper/', include('paper.urls')),
    path('api/review/', include('review.urls')),
    path('api/moderator/', include('moderation.urls')),
    path('api/main/', include('pages.urls')),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
