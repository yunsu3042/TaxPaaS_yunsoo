from rest_framework import serializers

from autoinput.models import Ten99INT, Ten99DIV, Ten99G, Ten99MISC, \
    Ten99Mortgage, Ten98EStudentLoanInterest, ChildCare

__all__ = ('Ten99INTSerializer', 'Ten99DIVSerializer', 'Ten99GSerializer',
           'Ten99MISCSerializer', 'Ten99MortgageSerializer',
           'Ten98EStudentLoanInterestSerializer','ChildCareSerializer')


class Ten99INTSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ten99INT
        fields = '__all__'


class Ten99DIVSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ten99DIV
        fields = '__all__'


class Ten99GSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ten99G
        fields = '__all__'


class Ten99MISCSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ten99MISC
        fields = '__all__'


class Ten99MortgageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ten99Mortgage
        fields = '__all__'


class Ten98EStudentLoanInterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ten98EStudentLoanInterest
        fields = '__all__'


class ChildCareSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChildCare
        fields = '__all__'
