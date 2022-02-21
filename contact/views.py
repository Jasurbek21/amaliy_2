from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Contact


# Create your views here.

class ContactView(CreateView):
    model = Contact
    fields = ("first_name", "last_name", "phone_number", "email", "message")
    success_url = reverse_lazy('xabarlar')
    template_name = 'home.html'

class ContactListView(ListView):
    model = Contact
    template_name = 'xabarlar.html'


