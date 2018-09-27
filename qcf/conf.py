# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy

SAVE_TO_DB = getattr(settings, 'QCF_SAVE_TO_DB', True)

TEMPLATES = getattr(settings, 'QCF_TEMPLATES', "default")

RECIPIENTS_LIST = getattr(settings, 'QCF_RECIPIENTS_LIST', [
                          settings.DEFAULT_FROM_EMAIL])

EMAIL_SENT_MESSAGE = getattr(
    settings, 'QCF_EMAIL_SENT_MESSAGE', _(u'Your message has been sent'))

REDIRECT_URL = getattr(settings, 'QCF_REDIRECT_URL',
                       reverse_lazy("contact-ok"))
