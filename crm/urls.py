from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.RedirectIndex, name='index'),
    path('instruction/', login_required(views.InstructionPage), name='instruction'),
    path('add_customer/', login_required(views.AddCustomerView.as_view()), name='add_customer'),
    path('customer_list/', login_required(views.CustomerList.as_view()), name='customer_list'),
    path('customer_detail/<int:pk>/', login_required(views.CustomerDetailView.as_view()), name='customer_detail'),
    path('update_customer/<int:pk>/', login_required(views.UpdateCustomerView.as_view()), name='update_customer'),
    path('delete_customer/<int:pk>/', login_required(views.DeleteCustomerView.as_view()), name='delete_customer'),
]