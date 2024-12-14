from django.contrib import admin
from .models import *

# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'locality', 'city', 'state')
    list_filter = ('city', 'state')
    list_per_page = 10
    search_fields = ('locality', 'city', 'state')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category_image', 'is_active', 'is_featured', 'updated_at')
    list_editable = ('slug', 'is_active', 'is_featured')
    list_filter = ('is_active', 'is_featured')
    list_per_page = 10
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug": ("title", )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'product_image', 'is_active', 'is_featured', 'updated_at')
    list_editable = ('slug', 'category', 'is_active', 'is_featured')
    list_filter = ('category', 'is_active', 'is_featured')
    list_per_page = 10
    search_fields = ('title', 'category', 'short_description')
    prepopulated_fields = {"slug": ("title", )}

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
    list_editable = ('quantity',)
    list_filter = ('created_at',)
    list_per_page = 20
    search_fields = ('user', 'product')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'status', 'ordered_date')
    list_editable = ('quantity', 'status')
    list_filter = ('status', 'ordered_date')
    list_per_page = 20
    search_fields = ('user', 'product')


@admin.register(TractorOperator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('operator_first_name', 'operator_last_name', 'operator_phone_number', 'operator_experience_years', 'operator_created_at')
    search_fields = ('operator_first_name', 'operator_last_name', 'operator_tractor_models_operated')



# Admin customization for the JobApplication model
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_first_name', 'applicant_desired_position', 'applicant_submitted_at')  # Ensure these fields exist in the model
    search_fields = ('applicant_first_name', 'applicant_first_name',)  # Searching by applicant name and related job posting title
    ordering = ('applicant_submitted_at', )  # To order applications by submission date (if 'submitted_at' exists)

# Admin customization for the JobPosting model
@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'category')  # Make sure these fields exist in your model
    search_fields = ('title', 'location', 'category')  # Allows searching by title, location, and related category name


@admin.register(InAppMessage)
class InAppMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'is_reply')  # Make sure these fields exist in your model
    search_fields = ('sender', 'recipient', 'is_reply')

admin.site.register(Address, AddressAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Skill)
