#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from rest_framework import routers

from .views import view_set_factory


class DRFRouter(routers.DefaultRouter):
    def register(self, prefix, viewset_or_model, base_name=None):
        if isinstance(viewset_or_model, models):
            viewset = view_set_factory(viewset_or_model)
        else:
            viewset = viewset_or_model
        return super(DRFRouter, self).register(prefix,
                                               viewset,
                                               base_name)
