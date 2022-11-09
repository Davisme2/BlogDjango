from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def PostList(request):
    post = Post.objects.filter(status=1).order_by('-created_on')
    context = {"posts": post}
    return render(request, "Blog/index.html", context)


def PostDetail(request, slug):
    # Detail article
    detail = Post.objects.get(slug=slug)
    category = detail.category
    recetteEnRelation = Post.objects.filter(category_id=category)
    # print(recetteRelation) liste de plat en relation

    # Liste de toutes le categories de plat
    cat = Category.objects.all()

    context = {"detail": detail, "recetteEnRelation": recetteEnRelation, "cat": cat}
    return render(request, "Blog/post_detail.html", context)
