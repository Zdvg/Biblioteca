from django.contrib import admin
from  django.urls import path 

from . import views 

urlpatterns = [
    path(
        'loan/add/',
        views.RegisterLoan.as_view(),
        name='loan-add'
    )
]