#import datatime
from django.db import models
from django.db.models import Count
from django.contrib.postgres.search import TrigramSimilarity

class BookManager(models.Manager):

    def book_list(self, kword):
        result = self.filter(
            title__icontains=kword,
            release_date__range=('2000-01-01','2005-01-01')
        )
        return 
    
    def book_list_trg(self, kword):
        if kword:
            result = self.filter(
            title__trigram_similar=kword, # funciona a partir de 4 palabras en el buscador
            )
            return result
        else:
            return self.all()[:10]
    
    def book_list2(self, kword, fecha1, fecha2):

        #date1 = datatime.datatime.strptime(fecha1, "%Y-%m-%d").date() y es esta la ue se pasa a release_date__range

        result = self.filter(
            title__icontains=kword,
            release_date__range=(fecha1,fecha2)
        )
        return result
    
    def book_list_category(self, category):
        return self.filter(
            category__id=category
        ).order_by('title')
    
    def add_author(self, book_id, author):
        book = self.get(id=book_id)
        book.authores.add(author) # para eliminar solo reemplazamos con "remove" (solo para casos de ManyToMany)
        return book
    
    def book_loan_num(self):
        result = self.aggregate(
            num_loan=Count('loan_book')
        )
        return result
    
    def num_books_loan(self):
        result = self.annotate(
            num_loan=Count('loan_book')
        )
        for r in result:
            print('===========')
            print(r, r.num_loan)
    

class CategoryManager(models.Manager):
    """ Manager para el modelo autor """

    def category_by_author(self, author):
        return self.filter(
            category_book__authores__id=author
        ).distinct()
    
    def category_books_list(self):
        result = self.annotate(
            num_books=Count('category_book')
        )
        return result