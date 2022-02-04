
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'news': News.objects.all()
    }
    return render(request, 'app/home.html', context)


class NewsListView(ListView):
    model = news
    template_name = 'app/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'news'
    ordering = ['-date_posted']
    paginate_by = 5


class NewsListView(ListView):
    model = News
    template_name = 'app/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(author=user).order_by('-date_posted')


class NewsDetailView(DetailView):
    model = News
    template_name = 'app/user_posts.html'  # <app>/<model>_<viewtype>.html


class SearchResultsListView(ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'news/search_results.html'
    queryset = News.objects.filter(title__icontains='beginners') # new










