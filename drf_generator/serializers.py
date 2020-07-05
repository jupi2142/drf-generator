#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Default serializer setting, they can specify their own serializer and
# view[set] class
# A separate serializer maker which also accepts mixins
# A separate viewset maker which also accepts mixins
# Expand?
from .settings import SERIALIZER


def serializer_factory(model, mixins=()):
    meta = type('Meta', (), {'fields': "__all__", 'model': model})
    return type('{}Serializer'.format(model.__name__),
                tuple(mixins) + (SERIALIZER,),
                {'Meta': meta})
