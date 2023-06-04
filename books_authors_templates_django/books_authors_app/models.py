from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Book(models.Model):
    author = models.ManyToManyField(Author, related_name="books")
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Books
def createBook(request):
    some_book = request.POST['bookTitle']
    some_book_desc = request.POST['bookDesc']
    create_book = Book.objects.create(title = some_book, desc = some_book_desc)
    return create_book

def getBook(request):
    some_book = Book.objects.all()
    return some_book

def getBookInfo(request, bookID):
    book_id = Book.objects.get(id = bookID)
    return book_id
#------------------------------------------
# Authors
def createAuthor(request):
    some_author_first_name = request.POST['authorFirstName']
    some_author_last_name = request.POST['authorLastName']
    some_author_note = request.POST['authorNote']
    create_author = Author.objects.create(first_name = some_author_first_name, last_name = some_author_last_name, note = some_author_note)
    return create_author

def getAuthor(request):
    some_author = Author.objects.all()
    return some_author

def getAuthorInfo(request, authorID):
    author_id = Author.objects.get(id = authorID)
    return author_id