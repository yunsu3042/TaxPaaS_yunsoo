from rest_framework import generics
from autoinput.models import SourceDoc
from rest_framework import permissions
from autoinput.serializers import SourceDocSerializer
from member.models import TaxPayerProfile
from rest_framework.response import Response
from rest_framework import status

__all__ = ('SourceDocDetailView', )


class SourceDocDetailView(generics.RetrieveAPIView):
    queryset = SourceDoc.objects.all()
    serializer_class = SourceDocSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        source_doc = self.get_fit_source_doc(request, *args, **kwargs)
        if source_doc is None:
            return Response({"errors": "요청하신 Source_doc이 없습니다"},
                            status=status.HTTP_404_NOT_FOUND)
        self.kwargs['source_doc'] = source_doc
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print("retrieve")
        instance = self.kwargs['source_doc']
        print(instance.tax_payer)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_fit_source_doc(self, request, *args, **kwargs):
        print("get_fit_source_doc")
        category = kwargs['category']
        doc_order = kwargs['doc_order']
        tax_payer = self.get_tax_payer(request)
        request.data._mutable = True
        request.data['tax_payer'] = tax_payer.pk
        source_docs = tax_payer.sourcedoc_set.filter(category=category).filter(
            doc_order=doc_order)
        if source_docs.exists():
            return source_docs[0]
        else:
            return None

    def get_tax_payer(self, request):
        print('get_tax_payer')
        user = request.user
        tax_payer = getattr(user, 'taxpayerprofile', None)
        if tax_payer is None:
            tax_payer = TaxPayerProfile.objects.create(user=user)
        return tax_payer
