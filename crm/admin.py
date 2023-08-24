from django.contrib import admin
from .models import Customer, Comment


# Registering the Customer model in the admin interface with custom display and search options
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'company', 'job_title', 'created_on', 'updated_on')
    search_fields = ['full_name', 'content', 'company']
    list_filter = ('company', 'created_on', 'updated_on')


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


# Registering the Comment model in the admin interface with custom display and actions
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'created_on', 'approved')
    list_filter = ('customer', 'approved')
    search_fields = ['name', 'body']

    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
