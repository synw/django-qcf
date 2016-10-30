# -*- coding: utf-8 -*-

from django.conf.urls import url
from qcf.views import AddPostView, AddPostRestView, OkPageView


urlpatterns = [
    url(r'^rest/$', AddPostRestView.as_view(), name="contact-rest"),
    url(r'^ok/$', OkPageView.as_view(), name="contact-ok"),
    url(r'^', AddPostView.as_view(), name="contact-post"),
    ]