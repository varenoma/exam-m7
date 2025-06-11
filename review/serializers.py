from rest_framework import serializers

from .models import Review


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('paper', 'journal', 'star', 'commit')


class ReviewListDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    journal = serializers.SerializerMethodField()
    paper = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('paper', 'journal', 'star', 'commit', 'created_at', 'author')
        read_only_fields = ('created_at', 'author')

    def get_author(self, obj):
        return obj.author.username if obj.author else None

    def get_journal(self, obj):
        return obj.journal.name if obj.journal else None

    def get_paper(self, obj):
        return obj.paper.name if obj.paper else None
