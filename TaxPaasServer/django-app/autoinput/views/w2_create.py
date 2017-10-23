from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from member.models import TaxPayerProfile

from autoinput.models import W2
from autoinput.serializers import SourceDocSerializer
from autoinput.serializers import W2Serializer

__all__ = ('W2CreateView', 'W2CreateView2')


## 유저 생성할 때 tax_payer설정해 줘야함
class W2CreateView(generics.CreateAPIView):
    queryset = W2.objects.all()
    serializer_class = W2Serializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        # self.check_img(request)
        request.data._mutable = True
        request.data['category'] = kwargs['category']
        request.data['order'] = kwargs['order']
        request.data['doc_order'] = kwargs['doc_order']
        request.data['source_doc'] = self.get_source_doc(request, *args, **kwargs)
        print(request.data)
        return self.w2_create(request, *args, **kwargs)

    def w2_create(self, request, *args, **kwargs):
        source_doc = request.data['source_doc']
        order = request.data['order']
        if source_doc:
            request.data['source_doc'] = request.data['source_doc'].pk
            if W2.objects.filter(source_doc=source_doc.pk).filter(order=order).exists():
                return Response({"errors": "이미 w2가 존재합니다 생성하고 싶다면 지우고 오세요"},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                return self.create(request, *args, **kwargs)
        else:
            return self.create_source_doc(request, *args, **kwargs)

    # source_doc 항목이 없을 경우 생성
    def create_source_doc(self, request, *args, **kwargs):
        serializer = SourceDocSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        source_doc = serializer.save()
        request.data['source_doc'] = source_doc.pk
        return self.create(request, *args, **kwargs)

    def get_source_doc(self, request, *args, **kwargs):
        category = request.data['category']
        doc_order = request.data['doc_order']
        tax_payer = self.get_tax_payer(request)
        request.data['tax_payer'] = tax_payer.pk
        source_docs = tax_payer.sourcedoc_set.filter(category=category).filter(
            doc_order=doc_order)
        if source_docs.exists():
            return source_docs[0]
        else:
            return None

    def check_img(self, request):
        if request.data.get('img', None) is None:
            return Response({'errors': "Img를 입력해이자식아"},
                            status=status.HTTP_400_BAD_REQUEST)
        return None

    def get_tax_payer(self, request):
        user = request.user
        tax_payer = getattr(user, 'taxpayerprofile', None)
        if tax_payer is None:
            tax_payer = TaxPayerProfile.objects.create(user=user)
        return tax_payer


class W2CreateView2(generics.CreateAPIView):
    queryset = W2.objects.all()
    serializer_class = W2Serializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        # self.check_img(request)
        request.data._mutable = True
        request.data['source_doc'] = self.get_source_doc(request, *args, **kwargs)
        print(request.data)
        return self.w2_create(request, *args, **kwargs)

    def w2_create(self, request, *args, **kwargs):
        source_doc = request.data['source_doc']
        order = request.data['order']
        if source_doc:
            request.data['source_doc'] = request.data['source_doc'].pk
            if W2.objects.filter(source_doc=source_doc.pk).filter(order=order).exists():
                return Response({"errors": "이미 w2가 존재합니다 생성하고 싶다면 지우고 오세요"},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                return self.create(request, *args, **kwargs)
        else:
            return self.create_source_doc(request, *args, **kwargs)

    # source_doc 항목이 없을 경우 생성
    def create_source_doc(self, request, *args, **kwargs):
        serializer = SourceDocSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        source_doc = serializer.save()
        request.data['source_doc'] = source_doc.pk
        return self.create(request, *args, **kwargs)

    def get_source_doc(self, request, *args, **kwargs):
        category = request.data['category']
        doc_order = request.data['doc_order']
        tax_payer = self.get_tax_payer(request)
        request.data['tax_payer'] = tax_payer.pk
        source_docs = tax_payer.sourcedoc_set.filter(category=category).filter(
            doc_order=doc_order)
        if source_docs.exists():
            return source_docs[0]
        else:
            return None

    def check_img(self, request):
        if request.data.get('img', None) is None:
            return Response({'errors': "Img를 입력해이자식아"},
                            status=status.HTTP_400_BAD_REQUEST)
        return None

    def get_tax_payer(self, request):
        user = request.user
        tax_payer = getattr(user, 'taxpayerprofile', None)
        if tax_payer is None:
            tax_payer = TaxPayerProfile.objects.create(user=user)
        return tax_payer