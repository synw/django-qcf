# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from qcf.views import AddPostView


urlpatterns = patterns('',
    url(r'^', AddPostView.as_view(), name="contact-post"),
)