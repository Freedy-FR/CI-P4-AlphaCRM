from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


# Urls patterns 
urlpatterns = [
    path('', views.RedirectIndexView.as_view(), name='index'),
    path('instruction/', views.InstructionPageView.as_view(), name='instruction'),
    path('add_customer/', views.AddCustomerView.as_view(), name='add_customer'),
    path('customer_list/', views.CustomerList.as_view(), name='customer_list'),
    path('about_me/', views.AboutMeView.as_view(), name='about_me'),
    path('customer_detail/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('update_customer/<int:pk>/', views.UpdateCustomerView.as_view(), name='update_customer'),
    path('delete_customer/<int:pk>/', views.DeleteCustomerView.as_view(), name='delete_customer'),    
]

# urlpatterns = [
#     path('', views.RedirectIndexView.as_view(), name='index'),
#     path('instruction/', login_required(views.InstructionPageView.as_view()), name='instruction'),
#     path('add_customer/', login_required(views.AddCustomerView.as_view()), name='add_customer'),
#     path('customer_list/', login_required(views.CustomerList.as_view()), name='customer_list'),
#     path('about_me/', views.AboutMeView.as_view(), name='about_me'),
#     path('customer_detail/<int:pk>/', login_required(views.CustomerDetailView.as_view()), name='customer_detail'),
#     path('update_customer/<int:pk>/', login_required(views.UpdateCustomerView.as_view()), name='update_customer'),
#     path('delete_customer/<int:pk>/', login_required(views.DeleteCustomerView.as_view()), name='delete_customer'),    
# ]