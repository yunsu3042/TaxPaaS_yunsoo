from rest_framework import serializers
from autoinput.models import SourceDoc

__all__ = ("SourceDocSerializer", )


class SourceDocSerializer(serializers.ModelSerializer):

    class Meta:
        model = SourceDoc
        fields = '__all__'
