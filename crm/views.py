from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import Customer
from .forms import AddCustomerForm, CommentForm
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
        comment_form = CommentForm()

        context = {
            "customer": customer,
            "comments": comments,
            "comment_form": comment_form,
        }

        return render(request, "customer_detail.html", context)

    def post(self, request, pk, *args, **kwargs):
        customer = get_object_or_404(Customer, pk=pk)
        comments = customer.comments.filter(approved=True).order_by("-created_on")

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.customer = customer
                comment.name = request.user.username
                comment.save()
        else:
            comment_form = CommentForm()

        context = {
            "customer": customer,
            "comments": comments,
            "comment_form": comment_form,
        }

        return render(request, "customer_detail.html", context)


class UpdateCustomerView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = AddCustomerForm
    template_name = 'update_customer.html'
    success_url = reverse_lazy('customer_list')
    

class DeleteCustomerView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'delete_customer.html'
    success_url = reverse_lazy('customer_list')


class RedirectIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})


class InstructionPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'instruction.html', {})
