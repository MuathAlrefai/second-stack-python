from django.db import models
from login_app.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.DO_NOTHING)
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.DO_NOTHING)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)