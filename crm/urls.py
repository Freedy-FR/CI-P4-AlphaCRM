from . import views
from django.urls import path

urlpatterns = [
    path('', views.CustomerList.as_view(), name="home"),
]
