# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class QcfConfig(AppConfig):
    name = "qcf"
    verbose_name = _(u"Contact form")
    
    def ready(self):
        pass