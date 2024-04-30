from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.utils.html import format_html
from django.urls import reverse

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'user', 'change_message']
    list_filter = ['action_flag', 'user', 'content_type']
    search_fields = ['object_repr', 'change_message']

    def object_link(self, obj):
        if obj.content_type is not None and obj.object_id is not None:
            link = reverse(
                f'admin:{obj.content_type.app_label}_{obj.content_type.model}_change',
                args=[obj.object_id]
            )
            return format_html('<a href="{}">{}</a>', link, obj.object_repr)
        return obj.object_repr

    object_link.short_description = 'Object'

admin.site.register(LogEntry, LogEntryAdmin)
