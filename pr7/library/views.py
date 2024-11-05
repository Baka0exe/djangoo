from django.shortcuts import render
from library.models.book import Book
from library.models.publisher import Publisher

# Create your views here.

def get_info(request):
    book = Book.objects.get(id=1)
    return render(request, 'base.html', context={
        'book' : book,
    })

def get_author(request):
    book_author = Book.objects.filter(author__name="Лев Николаевич Толстой")
    return render(request, 'author.html', context= {
        'book_author' : book_author,
    })
    
def get_author_info(request):
    author_info = Book.objects.exclude(author__name='Александр Сергеевич Пушкин')
    return render(request, 'author_info.html', context= {
        'author_info' : author_info
    })
    
def get_publisher(request):
    publisher_info = Publisher.objects.all()
    return render(request, 'publisher_info.html', context= {
        'publisher_info' : publisher_info
    })
    
    
    
def get_home(request):
    return render(request, 'home.html', context= {
        'title': 'Главная',
    })