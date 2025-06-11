import django_filters
from .models import Paper


class PaperFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(
        field_name='author__username', lookup_expr='icontains')
    keyword = django_filters.CharFilter(lookup_expr='icontains')
    reference = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Paper
        fields = ['name', 'author', 'keyword', 'reference']
