# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.conf.urls import url
from django.views.generic import RedirectView
from qcf.views import AddPostView, OkPageView


urlpatterns = [
    url(r'^ok/$', OkPageView.as_view(), name="contact-ok"),
    url(r'^mail/$', RedirectView.as_view(url=reverse_lazy('contact-post')),
        name='contact-index'),
    url(r'^$', AddPostView.as_view(), name="contact-post"),
]
