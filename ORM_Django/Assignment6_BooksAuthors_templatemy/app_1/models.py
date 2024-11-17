from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    
class Author(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    notes=models.TextField(default='no notes')
    books=models.ManyToManyField(Book,related_name='authors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



def save_book_data(data):
    Book.objects.create(title=data['title'],description=data['description'])
    
    
def show_book_data():
    book1=Book.objects.all()
    return book1


def save_author_data(data):
    Author.objects.create(fname=data['fname'],lname=data['lname'],notes=data['notes'])
    
    
    
def show_author_data():
    author1=Author.objects.all()
    return author1


def get_show_by_id_author(id):
    return Author.objects.get(id=id)

def get_show_by_id_book(id):
    return Book.objects.get(id=id)

def joinInAuthor(idbook,idauthor):
    
    a=Author.objects.get(id=idauthor)
    b=Book.objects.get(id=idbook)
    return a.books.add(b)
    
