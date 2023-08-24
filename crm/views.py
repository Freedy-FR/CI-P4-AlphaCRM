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
from django.contrib import messages


# Class for displaying the list of customers
class CustomerList(generic.ListView):
    customers = Customer.objects.all()
    model = Customer
    template_name = "customer_list.html"
    paginate_by = 10


# Class for adding a new customer
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
            messages.success(request, 'Customer added successfully.')
            return redirect('customer_list')
        else:
            messages.error(request, 'Error adding customer. Please check the form data.')
            return render(request, self.template_name, {'form': form})
       

# Class for viewing customer details and adding comments
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
                messages.success(request, 'Your comment is awaiting approval!')
                comment_form = CommentForm()
        else:
            comment_form = CommentForm()
            messages.error(request, 'Error adding comment. Please check your input.')

        context = {
            "customer": customer,
            "comments": comments,
            "comment_form": comment_form,
        }

        return render(request, "customer_detail.html", context)


# Class for updating customer information
class UpdateCustomerView(UpdateView):
    model = Customer
    form_class = AddCustomerForm
    template_name = 'update_customer.html'
    success_url = reverse_lazy('customer_list')

    def form_valid(self, form):
        messages.success(self.request, 'Customer updated successfully!')
        return super().form_valid(form)
    

# Class for deleting a customer
class DeleteCustomerView(DeleteView):
    model = Customer
    template_name = 'delete_customer.html'
    success_url = reverse_lazy('customer_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Customer deleted successfully!')
        return super().delete(request, *args, **kwargs)    


# Class for redirecting to the index page
class RedirectIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})


# Class for displaying the instruction page
class InstructionPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'instruction.html', {})


# Class for displaying the about me page
class AboutMeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about_me.html', {})


# Class for handling custom 404 error page
class Custom404View(View):
    def get(self, request, exception=None):
        return render(request, '404.html', status=404)
