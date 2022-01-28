from rest_framework import serializers
from rok.models.Resource import Resource

__all__ = ['ResourceSerializer']

class ResourceSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Resource
        fields = ('__all__')