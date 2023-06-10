from django.shortcuts import render, redirect
from login_app.models import User
from .models import Post, Comment

def make_post(request):
    user = User.objects.get(id=request.session['userid'])
    post = request.POST['user_post']
    Post.objects.create(user = user, post = post)
    return redirect('/wall')

def make_comment(request, ID):
    user = User.objects.get(id = request.session['userid'])
    post = Post.objects.get(id = ID)
    comment = request.POST['user_comment']
    Comment.objects.create(post = post, user = user, comment = comment)
    return redirect('/wall')

def wall(request):
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "posts": Post.objects.all().order_by("-created_at"),
        # "comments": Comment.objects.all().order_by("-created_at")
    }
    return render(request, 'wall.html', context)

def delete_post(request):
    post = Post.objects.get(id = request.POST['delete_post'])
    post.delete()
    return redirect('/wall')