from django.contrib import admin
from .models import TUIDUser

@admin.register(TUIDUser)
class TUIDUserAdmin(admin.ModelAdmin):

    list_display = ('name', 'uid', 'email', 'groups')
    readonly_fields = ('name', 'uid', 'email', 'groups')
    fields = readonly_fields
    search_fields = ['given_name', 'surname', 'uid']

    def has_add_permission(self, request, obj=None):
        return False

