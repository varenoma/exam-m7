from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Journal, JournalViewCount
from .serializers import JournalListSerializer, JournalCreateSerializer, JournalDetailSerializer
from .permissions import IsOwnerOrReadOnly


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_serializer_class(self):
        if self.action == "list":
            return JournalListSerializer
        elif self.action == "retrieve":
            return JournalDetailSerializer
        elif self.action == "create":
            return JournalCreateSerializer
        return JournalDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = Journal.objects.filter(author=user)

        is_verified = self.request.query_params.get('is_verified')
        if is_verified in ["true", "1"]:
            queryset = queryset.filter(is_verified=True)
        elif is_verified in ["false", "0"]:
            queryset = queryset.filter(is_verified=False)

        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'is_verified',
                openapi.IN_QUERY,
                description="Tasdiqlanganlarni korish (true yoki false)",
                type=openapi.TYPE_BOOLEAN
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        journal = get_object_or_404(Journal, pk=pk)
        user = request.user
        korilgan = JournalViewCount.objects.filter(
            journal=journal, user=user).exists()

        if not korilgan:
            journal.view_count += 1
            journal.save(update_fields=['view_count'])
            JournalViewCount.objects.create(journal=journal, user=user)

        serializer = JournalDetailSerializer(journal)
        return Response(serializer.data)


class AllJournalListAndDetail(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = [JournalListSerializer]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        return Journal.objects.filter(is_verified=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return JournalDetailSerializer
        return JournalListSerializer

    def retrieve(self, request, pk=None):
        journal = get_object_or_404(Journal, pk=pk, is_verified=True)
        user = request.user

        if user.is_authenticated:
            korilgan = JournalViewCount.objects.filter(
                journal=journal, user=user
            ).exists()

            if not korilgan:
                journal.view_count += 1
                journal.save(update_fields=['view_count'])
                JournalViewCount.objects.create(journal=journal, user=user)

        serializer = JournalDetailSerializer(journal)
        return Response(serializer.data)
