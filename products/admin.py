from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category', 'seller', 'category']
    list_display = ['name', 'category', 'owner']
    readonly_fields = ['date_created']

