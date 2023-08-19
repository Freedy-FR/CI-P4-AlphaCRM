from .models import Customer
from django import forms


class AddCustomerForm(forms.ModelForm):    
    full_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Full Name", "class":"form-control"}), label="")
    job_title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Job Title", "class":"form-control"}), label="")
    company = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Company", "class":"form-control"}), label="")
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
    country = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Country", "class":"form-control"}), label="")
    postcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Postcode", "class":"form-control"}), label="")
    content = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Customer Description", "class":"form-control"}), label="")
    
    class Meta:
        model = Customer
        exclude = ("user",)

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance

    