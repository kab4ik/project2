from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('index/', views.index, name='index'),
    #path('genres/', views.genre_list, name='genres'),
    path('genres/', views.GenreListView.as_view(), name='genres'),
    path('authors/', views.author_list, name='authors'),
    path('books/', views.book_list, name='books'),
    path('genre/<int:genre_id>/', views.genre_detail,
         name='genre_detail'),
    path('book/<int:book_id>/', views.book_detail,
         name='book_detail'),
    path('author/<int:author_id>/', views.author_detail,
         name='author_detail'),

]