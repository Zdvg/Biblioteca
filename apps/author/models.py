from django.db import models

# managers
from .managers import AuthorManager

# Create your models here.
class Person(models.Model):
    name = models.CharField(
        'Nombre',
        max_length=50
    )
    last_name = models.CharField(
        'Apellido',
        max_length=50
    )
    nationality = models.CharField(
        'Nacionalidad',
        max_length=50
    )
    age = models.IntegerField()

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.last_name
    
    class Meta:
        abstract = True
    
class  Author(Person):
    objects = AuthorManager()