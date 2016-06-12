# -*- coding: utf-8 -*-

from django.conf.urls import url
from qcf.views import AddPostView


urlpatterns = [
    url(r'^', AddPostView.as_view(), name="contact-post"),
    ]