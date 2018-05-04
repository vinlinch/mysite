from django.shortcuts import render
from  django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.template import loader, Context

from blog.models import BlogPost

# Create your views here.
def archive(request):
    posts = BlogPost.objects.all()
    # return HttpResponse(t.render(c))
    return render(request,'archive.html',{'posts':posts})


# Create your views here.
def blog_index(request):
    blog_list = BlogPost.objects.all()  # 获取所有数据
    return render(request,'blog.html', {'blog_list':blog_list})   # 返回index.html页面