from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.views.generic import ListView
from .models import Author

# Create your views here.
class AuthoresList(ListView):
    #model = Author
    template_name = 'author/authores_list.html'
    context_object_name = 'authores_list'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        return Author.objects.search_author2(palabra_clave)
