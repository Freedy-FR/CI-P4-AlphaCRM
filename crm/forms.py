from .models import Customer
from django import forms
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url


class AddCustomerForm(forms.ModelForm):
    full_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Full Name", "class":"form-control"}), label="")
    job_title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Job Title", "class":"form-control"}), label="")
    company = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Company", "class":"form-control"}), label="")
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
    country = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Country", "class":"form-control"}), label="")
    postcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Postcode", "class":"form-control"}), label="")
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "If needed add customer notes here...", "class": "form-control"}),label="")
    profile_picture = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={"class": "form-control"}),label="Profile Picture")

    
    class Meta:
        model = Customer
        exclude = ('author',)

    