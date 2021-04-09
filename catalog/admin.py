from django.contrib import admin
from .models import *

admin.site.register(Genre)
admin.site.register(Author)
#admin.site.register(Book)
admin.site.register(BookInstance)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genres_list')

admin.site.register(Book, BookAdmin)