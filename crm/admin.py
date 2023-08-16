from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'company', 'job_title',
                    'created_on', 'updated_on')
    search_fields = ['full_name', 'content', 'company']
    list_filter = ('company', 'created_on', 'updated_on')
