from rest_framework import serializers
from autoinput.models import SourceDoc
from autoinput.models import W2, Ten99G, Ten99MISC, Ten99INT, Ten99DIV,\
    Ten99Mortgage, Ten98EStudentLoanInterest, Ten98TTuitionStatement, ChildCare, Ten95B, Ten95C
from autoinput.serializers import W2Serializer, Ten99GSerializer, \
    Ten99MISCSerializer, Ten99INTSerializer, Ten99DIVSerializer, \
    Ten99MortgageSerializer, ChildCareSerializer, Ten95BSerializer, \
    Ten95CSerializer

__all__ = ("SourceDocSerializer", "SourceDocSerializer2", "SourceDocSerializer3")


class SourceDocSerializer(serializers.ModelSerializer):
    source_doc_list = serializers.SerializerMethodField()

    class Meta:
        model = SourceDoc
        fields = ('source_doc_list', 'tax_payer', 'category', 'doc_order')

    # source_list에 들어가는 내용이 많아진다면 수정요
    def get_source_doc_list(self, obj):
        context = {}
        doc_list = [W2, Ten99G, Ten99MISC, Ten99INT, Ten99DIV, Ten99Mortgage,
                    Ten98EStudentLoanInterest, Ten98TTuitionStatement,
                    ChildCare, Ten95B, Ten95C]
        for doc in doc_list:
            wanted_doc = doc.objects.filter(source_doc=obj)
            if wanted_doc.exists():
                count = wanted_doc.count()
            else:
                count = 0
            context[doc.__name__] = count
        return context


class SourceDocSerializer2(serializers.ModelSerializer):
    w2_list = serializers.SerializerMethodField()
    ten99g_list = serializers.SerializerMethodField()
    ten99misc_list = serializers.SerializerMethodField()
    ten99int_list = serializers.SerializerMethodField()
    ten99div_list = serializers.SerializerMethodField()
    ten99mortgage_list = serializers.SerializerMethodField()
    childcare_list = serializers.SerializerMethodField()
    ten95b_list = serializers.SerializerMethodField()
    ten95c_list = serializers.SerializerMethodField()

    class Meta:
        model = SourceDoc
        fields = ('w2_list', 'ten99g_list', 'ten99misc_list','ten99int_list',
                  'ten99div_list', 'ten99mortgage_list', 'childcare_list',
                  'ten95b_list', 'ten95c_list', 'tax_payer', 'category',
                  'doc_order')

    def get_w2_list(self, obj):
        w2_query = W2.objects.filter(source_doc=obj)
        serializer = W2Serializer(w2_query, many=True)
        return serializer.data

    def get_ten99g_list(self, obj):
        ten99g_query = Ten99G.objects.filter(source_doc=obj)
        serializer = Ten99GSerializer(ten99g_query, many=True)
        return serializer.data

    def get_ten99misc_list(self, obj):
        ten99mist_query = Ten99MISC.objects.filter(source_doc=obj)
        serializer = Ten99MISCSerializer(ten99mist_query, many=True)
        return serializer.data


    def get_ten99int_list(self, obj):
        ten99int_query = Ten99INT.objects.filter(source_doc=obj)
        serializer = Ten99INTSerializer(ten99int_query, many=True)
        return serializer.data


    def get_ten99div_list(self, obj):
        ten99div_query = Ten99DIV.objects.filter(source_doc=obj)
        serializer = Ten99DIVSerializer(ten99div_query, many=True)
        return serializer.data


    def get_ten99mortgage_list(self, obj):
        ten99mortgate_query = Ten99Mortgage.objects.filter(source_doc=obj)
        serializer = Ten99MortgageSerializer(ten99mortgate_query, many=True)
        return serializer.data


    def get_childcare_list(self, obj):
        childcare_query = ChildCare.objects.filter(source_doc=obj)
        serializer = ChildCareSerializer(childcare_query, many=True)
        return serializer.data


    def get_ten95b_list(self, obj):
        ten95b_query = Ten95B.objects.filter(source_doc=obj)
        serializer = Ten95BSerializer(ten95b_query, many=True)
        return serializer.data


    def get_ten95c_list(self, obj):
        ten95c_query = Ten95C.objects.filter(source_doc=obj)
        serializer = Ten95CSerializer(ten95c_query, many=True)
        return serializer.data


class SourceDocSerializer_min(serializers.Serializer):
    w2_list = serializers.SerializerMethodField()
    ten99g_list = serializers.SerializerMethodField()
    ten99misc_list = serializers.SerializerMethodField()
    ten99int_list = serializers.SerializerMethodField()
    ten99div_list = serializers.SerializerMethodField()
    ten99mortgage_list = serializers.SerializerMethodField()
    childcare_list = serializers.SerializerMethodField()
    ten95b_list = serializers.SerializerMethodField()
    ten95c_list = serializers.SerializerMethodField()

    class Meta:
        model = SourceDoc
        fields = (
        'w2_list', 'ten99g_list', 'ten99misc_list', 'ten99int_list',
        'ten99div_list', 'ten99mortgage_list', 'childcare_list',
        'ten95b_list', 'ten95c_list')

    def get_w2_list(self, obj):
        w2_query = W2.objects.filter(source_doc=obj)
        serializer = W2Serializer(w2_query, many=True)
        return serializer.data

    def get_ten99g_list(self, obj):
        ten99g_query = Ten99G.objects.filter(source_doc=obj)
        serializer = Ten99GSerializer(ten99g_query, many=True)
        return serializer.data

    def get_ten99misc_list(self, obj):
        ten99mist_query = Ten99MISC.objects.filter(source_doc=obj)
        serializer = Ten99MISCSerializer(ten99mist_query, many=True)
        return serializer.data

    def get_ten99int_list(self, obj):
        ten99int_query = Ten99INT.objects.filter(source_doc=obj)
        serializer = Ten99INTSerializer(ten99int_query, many=True)
        return serializer.data

    def get_ten99div_list(self, obj):
        ten99div_query = Ten99DIV.objects.filter(source_doc=obj)
        serializer = Ten99DIVSerializer(ten99div_query, many=True)
        return serializer.data

    def get_ten99mortgage_list(self, obj):
        ten99mortgate_query = Ten99Mortgage.objects.filter(source_doc=obj)
        serializer = Ten99MortgageSerializer(ten99mortgate_query,
                                             many=True)
        return serializer.data

    def get_childcare_list(self, obj):
        childcare_query = ChildCare.objects.filter(source_doc=obj)
        serializer = ChildCareSerializer(childcare_query, many=True)
        return serializer.data

    def get_ten95b_list(self, obj):
        ten95b_query = Ten95B.objects.filter(source_doc=obj)
        serializer = Ten95BSerializer(ten95b_query, many=True)
        return serializer.data

    def get_ten95c_list(self, obj):
        ten95c_query = Ten95C.objects.filter(source_doc=obj)
        serializer = Ten95CSerializer(ten95c_query, many=True)
        return serializer.data


class SourceDocSerializer3(serializers.ModelSerializer):
    results = serializers.SerializerMethodField()

    class Meta:
        model = SourceDoc
        fields = ('results', 'category', 'doc_order')

    def get_results(self, obj):
        source_doc = SourceDoc.objects.filter(pk=obj.pk)[0]
        serializer = SourceDocSerializer_min(source_doc)
        return serializer.data