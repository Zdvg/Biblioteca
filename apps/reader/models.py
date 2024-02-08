from django.db import models
from apps.book.models import Book
from apps.author.models import Person
from .managers import LoanManager

# Create your models here.
class Reader(Person):

    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'

class Loan(models.Model):
    reader = models.ForeignKey(
        Reader,
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='loan_book',
    )
    loan_date = models.DateField()
    return_date = models.DateField(
        blank=True,
        null=True
    )

    objects=LoanManager()

    def save(self, *args, **kwargs):
        super(Loan, self).save(*args, **kwargs)

    def __str__(self):
        return self.book.title + '-' + self.reader.name
