from rest_framework import viewsets
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import ReviewListDetailSerializer, ReviewCreateSerializer
from .models import Review


class ReviewViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        user = self.request.user
        queryset = Review.objects.all()

        mine = self.request.query_params.get('mine', '').strip().lower()
        journal_name = self.request.query_params.get(
            'journal_name', '').strip().lower()
        paper_name = self.request.query_params.get(
            'paper_name', '').strip().lower()

        if user.is_authenticated:
            if mine == 'true':
                queryset = queryset.filter(author=user)
            elif mine == 'false':
                queryset = queryset.exclude(author=user)

        if journal_name:
            queryset = queryset.filter(journal__name__icontains=journal_name)

        if paper_name:
            queryset = queryset.filter(paper__name__icontains=paper_name)

        return queryset

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReviewListDetailSerializer
        return ReviewCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('mine', openapi.IN_QUERY,
                              description="Mening reviewlarim", type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('journal_name', openapi.IN_QUERY,
                              description="Journal nomi bo'yicha qidirish", type=openapi.TYPE_STRING),
            openapi.Parameter('paper_name', openapi.IN_QUERY,
                              description="Paper nomi bo'yicha qidirish", type=openapi.TYPE_STRING),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
