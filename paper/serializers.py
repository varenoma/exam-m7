from rest_framework import serializers

from .models import Paper


class PaperListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username')

    class Meta:
        model = Paper
        fields = ('name', 'reference', 'keyword', 'author',
                  'view_count', 'created_at', 'pdf')


class PaperDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Paper
        fields = ('name', 'annotation', 'keyword', 'article', 'reference',
                  'author', 'pdf', 'view_count', 'is_verified', 'created_at')
        read_only_fields = ('author', 'view_count', 'created_at')


class PaperCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ('name', 'annotation', 'keyword',
                  'article', 'reference', 'pdf')
