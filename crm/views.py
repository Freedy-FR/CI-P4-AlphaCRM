from django.shortcuts import render, redirect
from django.views import generic
from .models import Customer
from django.contrib.auth.decorators import login_required


class CustomerList(generic.ListView):
    customers = Customer.objects.all()
    model = Customer
    template_name = "customer_list.html"
    paginate_by = 10


@login_required
def RedirectIndex(request):
    return render(request, 'index.html', {})


@login_required
def InstructionPage(request):
    return render(request, 'instruction.html', {})


# def RedirectIndex(request):
#     if request.user.is_authenticated:
#         return render(request, 'index.html', {})
#     else:
#         response = redirect('login')
#         return response


# def RedirectLogin(request):
#     response = redirect('/accounts/login/')
#     return response

# response = redirect('index')
# return response

# class CustomerList(generic.ListView):
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             queryset = Customer.objects.all().order_by('full_name')
#             model = Customer
#             template_name = "customer_list.html"
#             paginate_by = 20
#             return render(request, 'customer_list.html', {'queryset': queryset})
#         else:
#             return redirect('login')
