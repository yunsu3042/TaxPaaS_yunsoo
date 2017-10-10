from rest_framework import serializers
from autoinput.models import sourcedoc

__all__ = ("SourceDocSerializer", )


class SourceDocSerializer(serializers.ModelSerializer):

    class Meta:
        model = sourcedoc
        fields = '__all__'
