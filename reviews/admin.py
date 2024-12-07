from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ['rating']
    list_display = ['product', 'rating', 'owner']
    readonly_fields = ['date_created']
