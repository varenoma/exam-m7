from rest_framework import serializers

from .models import Contact


class ContactCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('first_name', 'email', 'message')
