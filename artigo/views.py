from django.shortcuts import render
from rest_framework import viewsets
from .api import PostSerializer

# Create your views here.
from .models import Post

# Create your views here.
def listar(request):
    return render(request, 'artigos_lista.html', {'posts': list(Post.objects.all())})


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('created_date')
    serializer_class = PostSerializer