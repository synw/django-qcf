# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django.http.response import Http404
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from qcf.models import Email
from qcf.forms import EmailForm
from qcf.conf import SAVE_TO_DB, RECIPIENTS_LIST, REDIRECT_URL


class OkPageView(TemplateView):
    template_name = "qcf/ok.html"
    
    def get_template_names(self):
        if not self.request.is_ajax():
            return ['qcf/ok.html']
        else:
            return ['qcf/rest_ok.html']
    

class AddPostView(CreateView):
    model = Email
    form_class = EmailForm
    
    def form_valid(self, form, **kwargs):
        if self.request.method == "POST":
            obj = form.save(commit=False)
            obj.email = form.cleaned_data['email']
            obj.subject = form.cleaned_data['subject']
            obj.content = form.cleaned_data['content']
            formated_request = ''
            for key in self.request.META.keys():
                formated_request += str(key)+' : '+str(self.request.META[key])+'\n'
            obj.request = formated_request
            #~ send mail
            send_mail(obj.subject, obj.content, obj.email, RECIPIENTS_LIST)
        else: 
            raise Http404
        if SAVE_TO_DB == True:
            return super(AddPostView, self).form_valid(form)
        else:
            return
        
    def get_template_names(self):
        if not self.request.is_ajax():
            return ['qcf/email_form.html']
        else:
            return ['qcf/rest_form.html']
        
            
    def get_success_url(self):
        return REDIRECT_URL


class AddPostRestView(AddPostView):
    
    def get_template_names(self):
        return ['qcf/rest_form.html']
    
    