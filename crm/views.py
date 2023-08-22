from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import Customer
from .forms import AddCustomerForm
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView


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


class CustomerDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        customer = get_object_or_404(Customer, pk=pk)
        comments = customer.comments.filter(approved=True).order_by("-created_on")

        return render(request, "customer_detail.html", {"customer": customer, "comments": comments,},)


class UpdateCustomerView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = AddCustomerForm
    template_name = 'update_customer.html'
    success_url = reverse_lazy('customer_list')
    

class DeleteCustomerView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'delete_customer.html'
    success_url = reverse_lazy('customer_list')




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
