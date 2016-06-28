# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from geoposition.fields import GeopositionField


class EMap(models.Model):
    name = models.CharField(max_length=100, verbose_name=_(u'Name'))
    position = GeopositionField(verbose_name=_(u'Position'))
    zoom = models.PositiveSmallIntegerField(blank=True, default=15, verbose_name=_(u'Zoom'))
    scale = models.PositiveSmallIntegerField(null=True, blank=True, default=2, verbose_name=_(u'Scale'))
    width = models.PositiveSmallIntegerField(null=True, blank=True, default=1000, verbose_name=_(u'Width'))
    height = models.PositiveSmallIntegerField(null=True, blank=True, default=500, verbose_name=_(u'Height'))
    html = models.TextField(blank=True, verbose_name=_(u'Text'))
    
    class Meta:
        verbose_name=_(u'Map')
        verbose_name_plural = _(u'Maps')

    def __unicode__(self):
        return self.name


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

    def __unicode__(self):
        return unicode(self.email+' : '+self.subject)

    

