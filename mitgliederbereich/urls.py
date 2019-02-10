from django.urls import path, include

from . import views

app_name = 'mitgliederbereich'

urlpatterns = [
    path('',views.MitgliedCreate.as_view(), name='createView'),
]
