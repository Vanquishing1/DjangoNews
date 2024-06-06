from django.urls import path
from .views import NewsDetailView
from .views import NewsListView, search_news, NewsCreateView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/search/', search_news, name='news_search'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/search/', search_news, name='news_search'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
]