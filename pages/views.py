from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from journal.models import Journal
from paper.models import Paper
from .serializers import MainSerializer


class MainAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        last_edition = Journal.objects.order_by('-created_at').first()
        most_read_paper = Paper.objects.order_by('-view_count')[:5]
        last_paper = Paper.objects.order_by('-created_at')[:4]

        data = {
            'last_edition': last_edition,
            'most_read_paper': most_read_paper,
            'last_paper': last_paper
        }

        serializer = MainSerializer(data)
        return Response(serializer.data)
