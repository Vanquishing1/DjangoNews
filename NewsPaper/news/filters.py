import django_filters
from .models import Post
from django import forms

class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    author = django_filters.CharFilter(lookup_expr='icontains', label='Author')
    created_at = django_filters.DateFilter(
        widget=forms.DateInput(attrs={'type': 'date'}),
        lookup_expr='gte',
        label='Created After'
    )

    class Meta:
        model = Post
        fields = ['title', 'author', 'created_at']

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains', label='Author')
    date_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}), label='Date After')

    class Meta:
        model = Post
        fields = ['title', 'author', 'date_after']
