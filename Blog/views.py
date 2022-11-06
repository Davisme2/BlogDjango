from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def PostList(request):
    post = Post.objects.filter(status=1).order_by('-created_on')
    context = {"posts": post}
    return render(request, "Blog/index.html", context)


def PostDetail(request, slug_post):
    return render(request, "Blog/post_detail.html")


