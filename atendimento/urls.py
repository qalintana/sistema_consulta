from django.contrib import admin
from django.urls import include, path

from .views import teste, teste2

app_name = 'atendimento'


urlpatterns = [
    path('', teste, name='teste'),
    path('dois/', teste2, name='teste2'),
]