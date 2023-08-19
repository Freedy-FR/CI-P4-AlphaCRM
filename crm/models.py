from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Customer(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer_record")
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

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return (f"{self.full_name} {self.company}")

