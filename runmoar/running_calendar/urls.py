# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import GetDateAPIView, ToggleStatusAPIView

urlpatterns = [
    url(r'^$', GetDateAPIView.as_view(), name='completionStatus'),
    url(r'^toggle$', ToggleStatusAPIView.as_view(), name='toggleStatus'),
]
