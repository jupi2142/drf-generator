#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers, viewsets


# A separate serializer maker which also accepts mixins
# A separate viewset maker which also accepts mixins
def SerializerFactory(model, mixins=()):
    mixins = list(mixins)
    mixins.append(serializers.HyperlinkedModelSerializer)

    class TheSerializer(mixins[0]):
        class Meta:
            fields = "__all__"

    TheSerializer.Meta.model = model

    return TheSerializer


def ViewSetFactory(model, serializer=None):
    class ViewSet(viewsets.ModelViewSet):
        pass

    ViewSet.queryset = model.objects.all()
    ViewSet.serializer_class = serializer or SerializerFactory(model)

    return ViewSet
