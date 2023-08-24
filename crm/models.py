from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Model for storing customer information
class Customer(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,related_name="customer_record",null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length=200, unique=True)
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    profile_picture = CloudinaryField('image', default='placeholder')
        

    class Meta:
        ordering = ["id"] # Order records by their ID

    def __str__(self):
        return (f"{self.full_name} {self.company}")


# Model for storing comments related to a customer
class Comment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"] # Order comments by their creation

    def __str__(self):
        return f"Comment {self.body} by {self.name}"