from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.RedirectIndex, name='index'),
    # path('accounts/login/', views.RedirectLogin, name='login'),
    path('customer_list/', login_required(views.CustomerList.as_view()), name='customer'),
    path('instruction/', views.InstructionPage, name='instruction'),
    path('add_customer/', views.AddCustomer.as_view(), name='add_customer'),

]
