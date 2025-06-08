from rest_framework import generics

from .serializer import ContactCreateSerializer
from .models import Contact

# Create your views here.


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCreateSerializer
