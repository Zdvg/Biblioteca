from django.db import models
from apps.author.models import Author
from .managers import BookManager, CategoryManager

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    objects = CategoryManager()

    def __str__(self):
        return str(self.id) + ' - ' + self.name
    

class Book(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category_book'
    )
    authores = models.ManyToManyField(Author)
    title = models.CharField(max_length=50)
    release_date = models.DateField('Fecha de Lanzamiento')
    front_page = models.ImageField(upload_to='portar')
    views = models.PositiveIntegerField()
    stok = models.PositiveIntegerField(default=0)

    objects = BookManager()

    class Meta:
        verbose_name='Libro'
        verbose_name_plural='Libros'
        db_table = 'libro'
        constraints = [ # barrera de validación para evitar recoger datos que no nos sirven
            models.CheckConstraint(check=models.Q(views__lt=18), name='views_menor_18')
        ]

    def __str__(self):
        return str(self.id) + ' - ' + self.title