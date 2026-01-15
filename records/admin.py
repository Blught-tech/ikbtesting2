from django.contrib import admin
from .models import Task, UserMFA
from django.contrib.admin.models import LogEntry

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # This tells the admin what columns to show in the list view
    list_display = ('title', 'owner', 'is_completed', 'created_at')
    # This adds a filter on the right side for better management
    list_filter = ('is_completed', 'owner')


@admin.register(UserMFA)
class UserMFAAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_enabled', 'enabled_at')
    list_filter = ('is_enabled',)

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    # This creates a searchable table for your audit logs
    list_display = ('action_time', 'user', 'content_type', 'object_repr', 'change_message')
    list_filter = ('user', 'action_flag')
    search_fields = ('change_message', 'object_repr')
    
    # Security: Ensure logs cannot be edited or deleted by anyone
    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False
    def has_delete_permission(self, request, obj=None): return False
