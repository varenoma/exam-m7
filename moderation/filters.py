import django_filters
from .models import Moderation


class ModerationFilter(django_filters.FilterSet):
    is_verified = django_filters.BooleanFilter()
    search = django_filters.CharFilter(
        field_name='description', lookup_expr='icontains')
    moder_username = django_filters.CharFilter(
        field_name='moder__username', lookup_expr='icontains')
    paper_author = django_filters.CharFilter(
        field_name='paper__author__username', lookup_expr='icontains')
    journal_author = django_filters.CharFilter(
        field_name='journal__author__username', lookup_expr='icontains')

    class Meta:
        model = Moderation
        fields = ['is_verified', 'search', 'moder_username',
                  'paper_author', 'journal_author']
