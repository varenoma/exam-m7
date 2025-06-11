from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Moderation
from .serializers import ModerationListSerializer, ModerationDetailUpdateSerializer
from .filters import ModerationFilter
from .permission import IsModerPermission


class ModerationViewSet(viewsets.ModelViewSet):
    queryset = Moderation.objects.all()
    permission_classes = [IsModerPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ModerationFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ModerationListSerializer
        return ModerationDetailUpdateSerializer

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('is_verified', openapi.IN_QUERY,
                          description="Tasdiqlanganmi?", type=openapi.TYPE_BOOLEAN),
        openapi.Parameter('search', openapi.IN_QUERY,
                          description="Description bo'yicha qidirish", type=openapi.TYPE_STRING),
        openapi.Parameter('moder_username', openapi.IN_QUERY,
                          description="Moder username bo'yicha qidirish", type=openapi.TYPE_STRING),
        openapi.Parameter('paper_author', openapi.IN_QUERY,
                          description="Paper muallifi username bo'yicha", type=openapi.TYPE_STRING),
        openapi.Parameter('journal_author', openapi.IN_QUERY,
                          description="Journal muallifi username bo'yicha", type=openapi.TYPE_STRING),
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        moderation = serializer.save(moder=self.request.user)
        if moderation.paper:
            moderation.paper.is_verified = moderation.is_verified
            moderation.paper.save()

    def perform_update(self, serializer):
        moderation = serializer.save()
        if moderation.paper:
            moderation.paper.is_verified = moderation.is_verified
            moderation.paper.save()
