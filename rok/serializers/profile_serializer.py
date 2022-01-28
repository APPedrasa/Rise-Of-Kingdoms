from rest_framework import serializers
from rok.models.Profile import Profile

__all__ = ['ProfileSerializer']

class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Profile
        fields = ('__all__')