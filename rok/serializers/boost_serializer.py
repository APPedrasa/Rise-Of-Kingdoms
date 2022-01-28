from rest_framework import serializers
from rok.models.Boost import Boost

__all__ = ['BoostSerializer']

class BoostSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Boost
        fields = ('__all__')