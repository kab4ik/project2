from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField('жанр', max_length=20)
    def __str__(self):
        return self.name
    def url(self):
        return reverse('catalog:genre_detail', args=(self.id,))

class Author(models.Model):
    last = models.CharField('фамилия', max_length=20)
    first = models.CharField('имя', max_length=20)
    date_of_birth = models.DateField('родился',
                                     blank=True, null=True)
    img = models.URLField('портрет', blank=True, null=True)
    def __str__(self):
        return f'{self.first} {self.last}'
    def url(self):
        return reverse('catalog:author_detail', args=(self.id,))
    def how_many_books(self):
        return len(self.book_set.all())
    class Meta:
        ordering = ['last']


class Book(models.Model):
    title = models.CharField('название', max_length=40)
    author = models.ForeignKey(Author, help_text='автор',
                               on_delete=models.SET_NULL, null=True, blank=True)
    genres = models.ManyToManyField(Genre, help_text='жанры')
    def  __str__(self):
        return self.title
    def genres_list(self):
        return ', '.join([genre.name for genre in self.genres.all()])
    def url(self):
        return reverse('catalog:book_detail', args=(self.id,))
    def avialable_instances(self):
        return [bi for bi in self.bookinstance_set.all() if bi.status == 'a']
    class Meta:
        ordering = ['title']


class BookInstance(models.Model):
    book = models.ForeignKey(Book, help_text='книга',
                             on_delete=models.SET_NULL, null=True)
    STATUSES = (
        ('o','на руках'), ('a','доступна'),
    )
    status = models.CharField(max_length=1, choices=STATUSES,
                              blank=True, default='а',
                              help_text='статус')
    def __str__(self):
        return f' экземпляр \"{self.book.title}\" (id={self.id})'


