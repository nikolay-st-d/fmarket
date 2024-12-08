from django.contrib import admin

from topics.models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated', 'updated_by')
    list_filter = ('updated_by',)
    readonly_fields = ('updated_by',)
