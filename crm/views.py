from django.shortcuts import render
from django.views import generic
from .models import Customer


class CustomerList(generic.ListView):
    model = Customer
    queryset = Customer.objects.all().order_by("-created_on")
    template_name = "index.html"
    paginate_by = 20
