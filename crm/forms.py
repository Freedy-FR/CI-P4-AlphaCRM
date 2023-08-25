from .models import Customer, Comment
from django import forms
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


# Form for adding a new customer
class AddCustomerForm(forms.ModelForm):
    full_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Full Name",
            "class": "form-control",
            "aria-label": "Full Name"  # Add ARIA label
        }),
        label="Full Name"
    )
    job_title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Job Title",
            "class": "form-control",
            "aria-label": "Job Title"  # Add ARIA label
        }),
        label="Job Title"
    )
    company = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Company",
            "class": "form-control",
            "aria-label": "Company"  # Add ARIA label
        }),
        label="Company"
    )
    email = forms.EmailField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Email",
            "class": "form-control",
            "aria-label": "Email"  # Add ARIA label
        }),
        label="Email"
    )
    address = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Address",
            "class": "form-control",
            "aria-label": "Address"  # Add ARIA label
        }),
        label="Address"
    )
    city = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "City",
            "class": "form-control",
            "aria-label": "City"  # Add ARIA label
        }),
        label="City"
    )
    country = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Country",
            "class": "form-control",
            "aria-label": "Country"  # Add ARIA label
        }),
        label="Country"
    )
    postcode = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Postcode",
            "class": "form-control",
            "aria-label": "Postcode"  # Add ARIA label
        }),
        label="Postcode"
    )
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "If needed add customer notes here...",
            "class": "form-control",
            "aria-label": "Customer Notes"  # Add ARIA label
        }),
        label="Customer Notes"
    )
    profile_picture = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control",
            "aria-label": "Profile Picture"  # Add ARIA label
        }),
        label="Profile Picture"
    )
    
    class Meta:
        model = Customer
        exclude = ('author',)


# Form for adding comments to a customer
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': 'Comment',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Using Crispy Forms to customize form layout
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
