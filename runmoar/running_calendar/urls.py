# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import GetDateAPIView

urlpatterns = [
    url(r'^$', GetDateAPIView.as_view(), name='completionStatus'),
]
