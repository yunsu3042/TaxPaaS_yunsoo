from rest_framework import generics
from rest_framework import permissions

from autoinput.functions import *
from autoinput.serializers import W2Serializer
from django.core.files.storage import default_storage as storage
from autoinput.models import W2


class W2CreateView(generics.CreateAPIView):
    queryset = W2.objcets.all()
    serializer_class = W2Serializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class W2UpdateVIew(generics.UpdateAPIView):
    queryset = W2.objects.all()
    serializer_class = W2Serializer
    permission_classes = (permissions.IsAuthenticated, )

    def put(self, request, *args, **kwargs):

        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwags):
        return self.partial_update(request, *args, **kwags)

#
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