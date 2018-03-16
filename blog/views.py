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