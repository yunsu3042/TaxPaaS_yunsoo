from rest_framework import serializers
from autoinput.models import SourceDoc
from autoinput.models import W2, Ten99G, Ten99MISC, Ten99INT, Ten99DIV,\
    Ten99Mortgage, Ten98EStudentLoanInterest, Ten98TTuitionStatement, ChildCare, Ten95B, Ten95C


__all__ = ("SourceDocSerializer", )


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