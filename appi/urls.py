from django.urls import path
from .views import PostList, PostDetail, SearchResultsListView,     PostListView,
    PostDetailView,

from . import views

urlpatterns = [

    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('', NewsListView.as_view(), name='news-home'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news-detail'),

]
