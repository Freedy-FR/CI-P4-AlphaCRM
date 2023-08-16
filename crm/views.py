from django.shortcuts import render
from django.views import generic
from .models import Customer


class CustomerList(generic.ListView):
    model = Customer
    queryset = Customer.objects.all()
    template_name = "index.html"
    paginate_by = 20
