from rest_framework import serializers
from autoinput.models import Ten95B, Ten95C

__all__ = ('Ten95BSerializer', 'Ten95CSerializer')


class Ten95BSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ten95B
        fields = '__all__'


class Ten95CSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ten95C
        fields = '__all__'
