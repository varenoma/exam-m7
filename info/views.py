from rest_framework import generics

from .models import FAQ, Requirement
from .serializers import FAQCreateSerializer, RequirementCreateSerializer


class FAQCreateView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQCreateSerializer


class RequirementCreateView(generics.ListAPIView):
    queryset = Requirement.objects.all()
    serializer_class = RequirementCreateSerializer
