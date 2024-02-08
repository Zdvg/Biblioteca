from django.db import models
from django.db.models import Q

class AuthorManager(models.Manager):
    """ Managers For Author Model """

    def search_author(self, kword):
        result = self.filter(
            name__icontains=kword
        )
        return result
    
    def search_author2(self, kword):
        result = self.filter(
            Q(name__icontains=kword) or Q(last_name__icontains=kword)
        )
        return result
    
    def search_author3(self, kword):
        result = self.filter(
            name__icontains=kword
        ).exclude(age=35)
        return result
    
    def search_author4(self, kword):
        result = self.filter(
            name__icontains=kword
        ).filter(
            Q(age__icontains=35) or Q(age__icontains=60)
        )
        return result
    
    def search_author5(self, kword):
        result = self.filter(
            edad__gt=40, # Mayor que Y
            edad__lt=65 # Menor que
        ).order_by('Apellido', 'Nombre', 'id')
        return result