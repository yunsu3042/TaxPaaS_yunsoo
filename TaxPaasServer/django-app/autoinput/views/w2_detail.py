import ast

from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from autoinput.models import W2
from autoinput.serializers import W2Serializer
from member.models import TaxPayerProfile

ast.literal_eval("{'x':1, 'y':2}")

__all__ = ('W2DetailView', 'W2DetailView2')


class W2DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = W2.objects.all()
    serializer_class = W2Serializer
    permission_classes = (permissions.IsAuthenticated, )

    # 나중에 url에 오는 단어를 기준으로 하나의 클래스에서 처리하게 할것
    # pk로 처리하게 되면 다른 사람의 개읹어보를 가져올 수 있기 때문에 큰일남

    def retrieve(self, request, *args, **kwargs):
        # request.data를 수정 가능하도록 코드 추가
        request.data._mutable = True
        request.data['category'] = kwargs['category']
        request.data['order'] = kwargs['order']
        request.data['doc_order'] = kwargs['doc_order']
        source_doc = self.get_source_doc(request, *args, **kwargs)
        if not source_doc:
            return Response({"errors": "요청한 유저의 SourceDoc이 존재하지 않습니다"},
                            status=status.HTTP_404_NOT_FOUND)
        elif source_doc:
            request.data['source_doc'] = source_doc.pk
        print("_"*70)
        print(source_doc)

        order = request.data['order']
        # 쿼리셋을 인스턴스화 하기 인덱스를 주어서
        instance = source_doc.w2_set.filter(order=order)[0]
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        order = kwargs.get("order", None)
        request.data._mutable = True
        request.data['category'] = kwargs['category']
        request.data['order'] = kwargs['order']
        request.data['doc_order'] = kwargs['doc_order']
        if order is None:
            print("order가 없다면")
            return Response({"error": "order를 입력하세요"},
                            status=status.HTTP_400_BAD_REQUEST)
        source_doc = self.get_source_doc(request, *args, **kwargs)
        print(source_doc)
        if not source_doc:
            return Response({"errors": "요청한 유저의 SourceDoc이 존재하지 않습니다"},
                            status=status.HTTP_404_NOT_FOUND)
        w2_set = source_doc.w2_set.filter(order=order)
        if w2_set is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        w2 = w2_set[0]
        self.kwargs['pk'] = w2.pk
        return self.update(request, *args, **kwargs)

    # put에서 유저 정보 입력받음
    def update(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk", None)
        if not pk:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['category'] = kwargs['category']
        request.data['order'] = kwargs['order']
        request.data['doc_order'] = kwargs['doc_order']
        order = kwargs.get("order", None)
        if order is None:
            print("order가 없다면")
            return Response({"error": "order를 입력하세요"},
                            status=status.HTTP_400_BAD_REQUEST)
        source_doc = self.get_source_doc(request, *args, **kwargs)
        print(source_doc)
        if not source_doc:
            return Response({"errors": "요청한 유저의 SourceDoc이 존재하지 않습니다"},
                            status=status.HTTP_404_NOT_FOUND)
        w2_set = source_doc.w2_set.filter(order=order)
        if not w2_set.exists():
            return Response({"errors": "요청한 w2가 존재하지 않습니다"},
                            status=status.HTTP_404_NOT_FOUND)
        w2 = w2_set[0]
        self.kwargs['pk'] = w2.pk
        return self.destroy(request, *args, **kwargs)

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

    def get_tax_payer(self, request):
        user = request.user
        tax_payer = getattr(user, 'taxpayerprofile', None)
        if tax_payer is None:
            tax_payer = TaxPayerProfile.objects.create(user=user)
        return tax_payer


class W2DetailView2(generics.RetrieveUpdateDestroyAPIView):
    queryset = W2.objects.all()
    serializer_class = W2Serializer
    permission_classes = (permissions.IsAuthenticated,)

    # 나중에 url에 오는 단어를 기준으로 하나의 클래스에서 처리하게 할것
    # pk로 처리하게 되면 다른 사람의 개읹어보를 가져올 수 있기 때문에 큰일남

    # put에서 유저 정보 입력받음
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


                # rdbs['1'] = ssn
# rdbs['8'] = EIN
# rdbs['2'] = first_name
# rdbs['3'] = last_name
# rdbs['4'] = state_zip[1]
# rdbs['7'] = state_zip[0]
# rdbs['5'] = street
# rdbs['6'] = city
# rdbs['9'] = employer_name
# rdbs['10'] = employer_zip
# rdbs['11'] = employer_street
# rdbs['12'] = employer_city
# rdbs['13'] = employer_state
# rdbs['14'] = wtc
# rdbs['15'] = fitw
# rdbs['16'] = ssw
# rdbs['17'] = sstw
# rdbs['18'] = mwat
# rdbs['19'] = mtw
# rdbs['20'] = sst
# rdbs['21'] = at
# rdbs['22'] = dcb
# rdbs['23'] = np
# rdbs['24'] = bx_12a
# rdbs['25'] = bx_12b
# rdbs['26'] = bx_12c
# rdbs['27'] = bx_12d
# rdbs['28'] = bx_13_se
# rdbs['29'] = bx_13_rp
# rdbs['30'] = bx_13_tpsp
# rdbs['31'] = bx_14_type
# rdbs['32'] = bx_14_amount
# rdbs['33'] = state
# rdbs['34'] = esin
# rdbs['35'] = swte
# rdbs['36'] = sit
# rdbs['37'] = ln
# rdbs['38'] = lwte
# rdbs['39'] = lit