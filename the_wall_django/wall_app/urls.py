from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall),
    # path('makepost', views.make_post)
]