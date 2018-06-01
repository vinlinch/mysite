from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Article
from datetime import datetime
from django.http import Http404
# Create your views here.

def home(request):
    post_list = Article.objects.all()
    return render(request, 'blog02/home.html', {'post_list':post_list})


def Test(request):
    # post = Article.objects.all()
    # return HttpResponse(post[0].content)
    return render(request, 'blog02/test.html', {'current_time':datetime.now()})

def Detail(request,id):
    try:
        post = Article.objects.get(id = int(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'blog02/post.html', {'post':post})
