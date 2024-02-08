from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path(
        'authors/',
        views.AuthoresList.as_view(),
        name="authores",
    ),
]