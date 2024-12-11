from django.contrib import admin
from terms.models import Term


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    readonly_fields = ['last_updated']
