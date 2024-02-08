from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path(
        'books/',
        views.BooksList.as_view(),
        name="books",
    ),
    path(
        'books-2/',
        views.BooksList2.as_view(),
        name="books2",
    ),
    path(
        'books-trg/',
        views.BooksListTrg.as_view(),
        name="books-trg",
    ),
    path(
        'books-details/<pk>',
        views.BooksDetailView.as_view(),
        name="books-details",
    ),
]