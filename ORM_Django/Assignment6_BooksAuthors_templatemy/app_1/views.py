from django.shortcuts import *
from . import models
def index(request):
    context={
        'books':models.show_book_data()
    }
    return render(request,'book.html',context)


def book(request):
    if request.method == 'POST':
        models.save_book_data(request.POST)
        return redirect('/')
    else:
        return HttpResponse("Error")






def author(request):
    context={
        'authoes':models.show_author_data()
    }
    return render(request,'author.html',context)


def author_save(request):
    if request.method == 'POST':
        models.save_author_data(request.POST)
        return redirect('/authors')
    else:
        return HttpResponse("Error")
    
    
def author_id(request,id):
    context={
        'author': models.get_show_by_id_author(id),
        'books':models.show_book_data()
        
        }
    return render(request,'resultForAuthor.html',context)


def book_id(request,id):
    context={
        'book': models.get_show_by_id_book(id),
        'authoes':models.show_author_data()
        
        }
    return render(request,'resultForBook.html',context)




def joinInAuthor(request,idbook,idauthor):
    context={
        'author1': models.get_show_by_id_author(id),
        'book1': models.get_show_by_id_book(id),
        'join':models.joinInAuthor(idbook,idauthor)
    }
    return render(request,'resultForBook.html',context)