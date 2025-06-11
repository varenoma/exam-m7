from rest_framework import serializers

from .models import Moderation


class ModerationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderation
        fields = ('description', 'star', 'paper', 'is_verified')


class ModerationDetailUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderation
        fields = ('description', 'star', 'paper',
                  'journal', 'created_at', 'is_verified')
        read_only_fields = ('created_at',)
