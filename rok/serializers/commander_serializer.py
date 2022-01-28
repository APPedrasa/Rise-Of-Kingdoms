from rest_framework import serializers
from rok.models.Commander import Commander

__all__ = ['CommanderSerializer']

class CommanderSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Commander
        fields = ('__all__')