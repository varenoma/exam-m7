from rest_framework import serializers

from .models import Journal


class JournalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('name', 'image', 'description', 'technologies')


class JournalDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Journal
        fields = ('name', 'description', 'pdf',
                  'author', 'technologies', 'image', 'view_count', 'created_at')
        read_only_fields = ('author', 'view_count', 'created_at')


class JournalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('name', 'description', 'pdf',
                  'technologies', 'image',)
