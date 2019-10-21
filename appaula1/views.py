from django.http import HttpResponse
from django.shortcuts import render


def blog(request,postid):
    return HttpResponse('Hello, Blog! %s' % postid)

def pages(request):
    return HttpResponse('Paginas Amarelas!')

def home(request):
    return HttpResponse('Home, World!')

def post_list(request):
    return render(request, 'post_list.html', {})