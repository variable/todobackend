from django.contrib import admin
from .models import TODOItem

class TODOItemAmin(admin.ModelAdmin):
    list_display = ['uuid', 'session_id', 'description', 'priority', 'created_at', 'completed_at']

admin.site.register(TODOItem, TODOItemAmin)
