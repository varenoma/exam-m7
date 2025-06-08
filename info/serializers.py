from rest_framework import serializers

from .models import FAQ, Requirement


class FAQCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('name', 'description')


class RequirementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ('name', 'description')
