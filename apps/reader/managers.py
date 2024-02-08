from django.db import models
from django.db.models import Avg, Sum, Count

class LoanManager(models.Manager):
    """ Loan procedures """

    def book_mean_age(self):
        result = self.filter(
            book__id='15'
        ).aggregate(
            mean_age=Avg('reader__age'),
            sum_age=Sum('reader__age')
        )
        return result
    
    def num_books_loan(self):
        result = self.values(
            'book'
        ).annotate(
            num_loan=Count('book')
        )
        for r in result:
            print('===========')
            print(r, r.num_loan)