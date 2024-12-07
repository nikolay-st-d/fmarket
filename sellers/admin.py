from django.contrib import admin
from sellers.models import Seller


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_filter = ['approved',]
    list_display = ['name', 'city', 'approved', 'account']
    readonly_fields = ['account']
