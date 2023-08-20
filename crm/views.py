from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import Customer
from .forms import AddCustomerForm
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url


class CustomerList(generic.ListView):
    customers = Customer.objects.all()
    model = Customer
    template_name = "customer_list.html"
    paginate_by = 10


class AddCustomerView(View):
    template_name = 'add_customer.html'

    def get(self, request):
        form = AddCustomerForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddCustomerForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('customer_list') 
        return render(request, self.template_name, {'form': form})


    


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
