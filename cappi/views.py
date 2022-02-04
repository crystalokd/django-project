from rest_framework import generics, permissions 

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer


class NewsList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthorOrReadOnly,) 
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class NewsListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']


    class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer