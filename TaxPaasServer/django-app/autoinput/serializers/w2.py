from rest_framework import serializers
from autoinput.models import W2

__all__ = ('W2Serializer', )


class W2Serializer(serializers.ModelSerializer):

    class Meta:
        model = W2
        fields = '__all__'
