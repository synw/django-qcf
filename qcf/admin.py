# -*- coding: utf-8 -*-

from django.contrib import admin
from qcf.models import Email
from qcf.forms import EmailAdminForm


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    form = EmailAdminForm
    search_fields = ('message', 'subject')
    date_hierarchy = 'created'
    list_display = ('email', 'subject', 'created')
    
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = ('created', 'email', 'subject', 'content')
        if request.user.is_superuser:
            readonly_fields += ('request',)
        return readonly_fields