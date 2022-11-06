from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList, name='home'),
    path('recette/<str:post_slug>', views.PostDetail, name='post_detail'),
]
