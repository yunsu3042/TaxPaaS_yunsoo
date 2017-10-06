from rest_framework import serializers
from autoinput.models import sourcedoc


class SourceDocSerializer(serializers.ModelSerializer):

    class Meta:
        model = sourcedoc
        fields = '__all__'
