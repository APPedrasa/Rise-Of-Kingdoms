from rest_framework import serializers
from rok.models.Kill import Kill

__all__ = ['KillSerializer']

class KillSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Kill
        fields = ('__all__')