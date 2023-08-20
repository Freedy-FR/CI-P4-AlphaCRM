from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.RedirectIndex, name='index'),
    path('instruction/', views.InstructionPage, name='instruction'),
    path('add_customer/', views.AddCustomerView.as_view(), name='add_customer'),
    path('customer_list/', views.CustomerList.as_view(), name='customer_list')
]