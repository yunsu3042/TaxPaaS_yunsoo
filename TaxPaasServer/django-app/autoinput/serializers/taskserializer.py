from autoinput.models import Task
from rest_framework import serializers

__all__ = ('TaskSerializer', )


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'