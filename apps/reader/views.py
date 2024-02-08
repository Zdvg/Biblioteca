from datetime import date

from django.shortcuts import render
from django.views.generic.edit import FormView

from .models import Loan
from .forms import LoanForm

# Create your views here.
class RegisterLoan(FormView):
    template_name = 'reader/add_loan.html'
    form_class = LoanForm
    success_url = '.'

    def form_valid(self, form):
        # Loan.objects.create(
        #     reader = form.cleaned_data['reader'],
        #     book = form.cleaned_data['book'],
        #     loan_date = date.today(),
        #     return_book = False
        # )
        loaan = Loan(
            reader = form.cleaned_data['reader'],
            book=form.cleaned_data['book'],
            loan_date=date.today(),
        )
        loaan.save()

        book = form.cleaned_data['book']
        book.stok = book.stok - 1
        book.save()
        return super(RegisterLoan, self).form_valid(form)
    
class AddLoan(FormView):
    template_name = "reader/add_loan.html"
    form_class = LoanForm
    success_url = '.'

    def form_valid(self, form):
        obj, created = Loan.objects.get_or_create(
            reader=form.cleaned_data['reader'], 
            book=form.cleaned_data['book'],
            defaults={
                'loan_date': date.today()
            }
        )
        return super(AddLoan, self).form_valid(form)