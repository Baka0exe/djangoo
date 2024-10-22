from django.shortcuts import render
from library.models.book import Book

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