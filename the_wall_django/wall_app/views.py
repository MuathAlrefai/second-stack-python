from django.shortcuts import render, redirect
from login_app import models
from .models import Post, Comment

def make_post(request):
    user = models.user_session_model(request)
    post = request.POST['user_post']
    models.Post.objects.create(user = user, post = post)
    return redirect('/wall')

def wall(request):
    context = {
        "user": models.user_session_model(request),
        "posts": Post.objects.all()
    }
    return render(request, 'wall.html', context)
