from django.contrib import admin

from .models import Loan, Reader

# Register your models here.
admin.site.register(Loan)
admin.site.register(Reader)
