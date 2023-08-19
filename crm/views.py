from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import AddCustomerForm


class CustomerList(generic.ListView):
    customers = Customer.objects.all()
    model = Customer
    template_name = "customer_list.html"
    paginate_by = 10


class AddCustomer(FormView):
    template_name = 'add_customer.html'
    form_class = AddCustomerForm
    success_url = reverse_lazy('/customer_list/') 

    def form_valid(self, form):
        form.save(user=self.request.user)
        return super().form_valid(form)


    


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
