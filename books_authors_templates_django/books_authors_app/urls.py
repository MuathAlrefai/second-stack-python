from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('addBook', views.addBook),
    path('authors', views.authors),
    path('addAuthor', views.addAuthor),
    path('bookDetails/<int:bookID>', views.bookDetails),
    path('authorDetails/<int:authorID>', views.authorDetails)
]