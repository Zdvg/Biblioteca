from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Book

# Create your views here.
class BooksList(ListView):
    template_name = 'book/list.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        key_word = self.request.GET.get("kword", '')
        date1 = self.request.GET.get("fecha1", '')
        date2 = self.request.GET.get("fecha2", '')

        if date1 and date2:
            return Book.objects.book_list2(key_word, date1, date2)
        else:
            return Book.objects.book_list(key_word)
        
class BooksListTrg(ListView):
    template_name = 'book/list.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        key_word = self.request.GET.get("kword", '')
        return Book.objects.book_list_trg(key_word)
        
class BooksList2(ListView):
    template_name = 'book/list2.html'
    context_object_name = 'book_list2'

    def get_queryset(self):
        return Book.objects.book_list_category('4')
    

class BooksDetailView(DetailView):
    model = Book
    template_name = 'book/detail.html'