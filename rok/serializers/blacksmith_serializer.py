from rest_framework import serializers
from rok.models.Blacksmith import Blacksmith

__all__ = ['BlacksmithSerializer']

class BlacksmithSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Blacksmith
        fields = ('__all__')