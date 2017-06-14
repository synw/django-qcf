# -*- coding: utf-8 -*-

from django import forms
from qcf.models import Email


class EmailForm(forms.ModelForm):
    
    class Meta:
        model = Email
        fields = ['email', 'subject', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 8, 'style':'width:100% !important;max-width:100% !important;'}),
            }
        
      
class EmailAdminForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email', 'subject', 'content']


