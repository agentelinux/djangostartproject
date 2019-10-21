from django.shortcuts import render

# Create your views here.
from .models import Post

# Create your views here.
def listar(request):
    return render(request, 'artigos_lista.html', {'posts': list(Post.objects.all())})