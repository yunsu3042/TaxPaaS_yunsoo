import ast

from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from autoinput.models import W2
from autoinput.serializers import W2Serializer
from member.models import TaxPayerProfile

ast.literal_eval("{'x':1, 'y':2}")

__all__ = ('W2DetailView', )


class W2DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = W2.objects.all()
    serializer_class = W2Serializer
    permission_classes = (permissions.IsAuthenticated, )

    # 나중에 url에 오는 단어를 기준으로 하나의 클래스에서 처리하게 할것
    # pk로 처리하게 되면 다른 사람의 개읹어보를 가져올 수 있기 때문에 큰일남

    def retrieve(self, request, *args, **kwargs):
        source_doc = self.find_source_doc(request, *args, **kwargs)
        w2 = source_doc.w2_set.all()
        print(w2)
        if not w2:
            return Response({"detail": "요청한 w2가 존재하지 않습니다"},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            instance = w2
            serializer = self.get_serializer(instance, many=True)
            return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        source_doc = self.find_source_doc(request, *args, **kwargs)
        try:
            w2 = source_doc.w2_set.all()[0]
        except IndexError:
            return Response({"detail": "요청한 w2가 존재하지 않습니다"},
                            status=status.HTTP_404_NOT_FOUND)
        self.kwargs['pk'] = w2.pk
        return self.update(request, *args, **kwargs)

    # user 확인 작업할 것
    def update(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk", None)
        if not pk:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        source_doc = self.find_source_doc(request, *args, **kwargs)
        try:
            w2 = source_doc.w2_set.all()[0]
        except IndexError:
            return Response({"detail": "요청한 w2가 존재하지 않습니다"},
                            status=status.HTTP_404_NOT_FOUND)
        self.kwargs['pk'] = w2.pk
        return self.destroy(request, *args, **kwargs)

    def find_source_doc(self, request, *args, **kwargs):
        user = request.user
        tax_payer = getattr(user, 'taxpayerprofile', None)
        if not tax_payer:
            tax_payer = TaxPayerProfile.objects.create(user=user)
        source_doc_set = getattr(tax_payer, 'sourcedoc_set', None)
        if not source_doc_set.all():
            return Response({"errors": "w2 does not exists"},
                            status=status.HTTP_404_NOT_FOUND)
        category = kwargs.get('category', None)
        if not category:
            return Response({"errors": "You must send category"},
                            status=status.HTTP_400_BAD_REQUEST)
        source_doc = source_doc_set.filter(category=category)[0]
        return source_doc






# rdbs['1'] = ssn
# rdbs['2'] = first_name
# rdbs['3'] = last_name
# rdbs['4'] = state_zip[1]
# rdbs['5'] = street
# rdbs['6'] = city
# rdbs['7'] = state_zip[0]
# rdbs['8'] = EIN
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