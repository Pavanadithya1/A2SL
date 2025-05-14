from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Custom User Admin with limited permissions
class UserAdmin(BaseUserAdmin):
    # Restrict what fields can be edited
    readonly_fields = ('date_joined', 'last_login')

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

# Unregister the default User admin
admin.site.unregister(User)

# Register our custom User admin
admin.site.register(User, UserAdmin)

# Similarly restrict Group permissions
class GroupAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)