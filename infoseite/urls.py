from django.urls import path, include

from . import views

app_name = 'infoseite'

urlpatterns = [
    path('',views.index,name='index'),
]
