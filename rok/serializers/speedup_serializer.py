from rest_framework import serializers
from rok.models.Speedup import Speedup

__all__ = ['SpeedupSerializer']

class SpeedupSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Speedup
        fields = ('__all__')