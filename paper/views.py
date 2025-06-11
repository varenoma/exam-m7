from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from .models import Paper, PaperViewCount
from .serializers import PaperListSerializer, PaperCreateSerializer, PaperDetailSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import PaperFilter


class PaperViewSet(viewsets.ModelViewSet):
    queryset = Paper.objects.all()
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_serializer_class(self):
        if self.action == "list":
            return PaperListSerializer
        elif self.action == "retrieve":
            return PaperDetailSerializer
        elif self.action == "create":
            return PaperCreateSerializer
        return PaperDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = Paper.objects.filter(author=user)

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
                description="Tasdiqlanganlarni ko'rish (true yoki false)",
                type=openapi.TYPE_BOOLEAN
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        paper = get_object_or_404(Paper, pk=pk)
        user = request.user
        korilgan = PaperViewCount.objects.filter(
            paper=paper, user=user).exists()

        if not korilgan:
            paper.view_count += 1
            paper.save(update_fields=['view_count'])
            PaperViewCount.objects.create(paper=paper, user=user)

        serializer = PaperDetailSerializer(paper)
        return Response(serializer.data)


class AllPaperListAndDetail(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        queryset = Paper.objects.filter(is_verified=True)
        name = self.request.query_params.get('name', None)
        author = self.request.query_params.get('author', None)
        keyword = self.request.query_params.get('keyword', None)
        reference = self.request.query_params.get('reference', None)

        if name or author or keyword or reference:
            queryset = queryset.filter(
                Q(name__icontains=name) if name else Q(),
                Q(author__username__icontains=author) if author else Q(),
                Q(keyword__icontains=keyword) if keyword else Q(),
                Q(reference__icontains=reference) if reference else Q()
            )

        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PaperDetailSerializer
        return PaperListSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY,
                              description="Nom bo'yicha qidirish", type=openapi.TYPE_STRING),
            openapi.Parameter('author', openapi.IN_QUERY,
                              description="Muallif bo'yicha qidirish", type=openapi.TYPE_STRING),
            openapi.Parameter('keyword', openapi.IN_QUERY,
                              description="Keyword bo'yicha qidirish", type=openapi.TYPE_STRING),
            openapi.Parameter('reference', openapi.IN_QUERY,
                              description="Reference bo'yicha qidirish", type=openapi.TYPE_STRING),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        paper = get_object_or_404(Paper, pk=pk, is_verified=True)
        user = request.user

        if user.is_authenticated:
            korilgan = PaperViewCount.objects.filter(
                paper=paper, user=user
            ).exists()

            if not korilgan:
                paper.view_count += 1
                paper.save(update_fields=['view_count'])
                PaperViewCount.objects.create(paper=paper, user=user)

        serializer = PaperDetailSerializer(paper)
        return Response(serializer.data)
