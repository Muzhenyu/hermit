from . import models
from rest_framework import serializers

class AreaInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Areas
        fields=('id','name')

class NextAreasInfoSeria(serializers.ModelSerializer):
    addinfos=AreaInfoSerializer(many=True,read_only=True)
    class Meta:
        model=models.Areas
        fields=('id','name','addinfos')


class AreaSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Areas
        fields=('name',)

class showdistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Areas
        fields=('name','id')
class showstreetSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Areas
        fields=('name','id')