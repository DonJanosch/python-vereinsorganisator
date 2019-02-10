from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Mitglied

class MitgliedCreate(CreateView):
    model = Mitglied
    fields = ['first_name','last_name','email','phone']
