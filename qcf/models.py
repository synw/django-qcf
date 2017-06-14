# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Email(models.Model):
    email = models.EmailField(verbose_name=_(u'Email'))
    subject = models.CharField(max_length=255, verbose_name=_(u'Subject'))
    content = models.TextField(verbose_name=_(u'Message'))
    # meta info
    created = models.DateTimeField(auto_now_add=True, verbose_name=_(u'Date posted'))
    request = models.TextField()
    
    class Meta:
        verbose_name=_(u'Email')
        verbose_name_plural = _(u'Emails')
        ordering = ('-created',)

    def __str__(self):
        return self.email+' : '+self.subject