from rest_framework import serializers
from journal.models import Journal
from paper.models import Paper


class PaperShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ['name', 'annotation']


class PaperFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ['id', 'name', 'annotation', 'created_at']


class JournalShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'name', 'description', 'created_at']


class MainSerializer(serializers.Serializer):
    last_edition = JournalShortSerializer()
    most_read_paper = PaperShortSerializer(many=True)
    last_paper = PaperFullSerializer(many=True)
