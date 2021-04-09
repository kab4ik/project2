from django.shortcuts import render
from .models import *
from django.views.generic import ListView

def index(request):
    context = {
        'n_genres': Genre.objects.all().count(),
        'n_authors': Author.objects.all().count(),
        'n_books': len(Book.objects.all()),
    }
    return render(request, 'catalog/index.html',
                  context)

# def genre_list(request):
#     context = {
#         'genres': Genre.objects.all(),
#     }
#     return render(request, 'catalog/genre_list.html',
#                   context)
class GenreListView(ListView):
    model = Genre
    context_object_name = 'genres'



def author_list(request):
    context = {
        'authors': sorted(Author.objects.all(), key=lambda x: (-x.how_many_books(), x.last),
                          ),
    }
    return render(request, 'catalog/author_list.html',
                  context)
def book_list(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'catalog/book_list.html',
                  context)


def genre_detail(request, genre_id):
    context = {
        'genre': Genre.objects.get(pk=genre_id),
    }
    return render(request, 'catalog/genre_detail.html',
                  context)


def book_detail(request, book_id):
    context = {
        'book': Book.objects.get(pk=book_id),
    }
    return render(request, 'catalog/book_detail.html',
                  context)


def author_detail(request, author_id):
    context = {
        'author': Author.objects.get(pk=author_id),
    }
    return render(request, 'catalog/author_detail.html',
                  context)

