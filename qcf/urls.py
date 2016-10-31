# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.conf.urls import url
from django.views.generic import RedirectView
from qcf.views import AddPostView, AddPostRestView, OkPageView


urlpatterns = [
    url(r'^rest/$', AddPostRestView.as_view(), name="contact-rest"),
    url(r'^ok/$', OkPageView.as_view(), name="contact-ok"),
    url(r'^mail/$', RedirectView.as_view(url=reverse_lazy('contact-post')), name='index'),
    url(r'^$', AddPostView.as_view(), name="contact-post"),
    ]