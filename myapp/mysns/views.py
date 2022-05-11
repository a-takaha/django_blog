from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

def index(request):
    posts = Posts.objects.all()
    context = {
        "message": "初めてのDjangoアプリ作成",
        "posts": posts,
        }
    return render(request, "mysns/index.html", context)
