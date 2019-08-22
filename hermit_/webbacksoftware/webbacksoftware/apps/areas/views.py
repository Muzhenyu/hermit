from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import RetrieveAPIView,ListAPIView
from . import models
from . import serializers
from rest_framework_extensions.cache.mixins import CacheResponseMixin
import logging
log=logging.getLogger('code')
log.debug('code_log')
# Create your views here.
class AreasViewSet(ReadOnlyModelViewSet,CacheResponseMixin):

    def get_queryset(self):
        if self.action=='list':
            return models.Areas.objects.filter(pid=None)
        else:
            # return models.Areas.objects.filter(pid=130000)
            return models.Areas.objects.all()
    def get_serializer_class(self):
        if self.action=='list':
            return serializers.AreaInfoSerializer
        else:
            return serializers.NextAreasInfoSeria

class showdistrictView(ListAPIView):
    serializer_class = serializers.showdistrictSerializer
    def get_queryset(self):
        return models.Areas.objects.filter(pid=None)

class showstreetView(ListAPIView):
    serializer_class = serializers.showstreetSerializer
    def get_queryset(self):
        return models.Areas.objects.exclude(pid=None).order_by('?')[:9]


class AreasSearchView(ListAPIView):
    serializer_class = serializers.AreaSearchSerializer
    def get_queryset(self):
        search_condition=self.request.query_params['area']
        return models.Areas.objects.filter(name__regex=search_condition)

