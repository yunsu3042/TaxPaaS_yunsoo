import django_rq
from PIL import Image
from django.core.files.storage import default_storage as storage
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from autoinput.functions.w2 import autocomplete
from autoinput.models import W2
from autoinput.serializers import TaskSerializer
from autoinput.serializers import W2Serializer
from autoinput.task_func import Task
from autoinput.task_func import w2_autocomplete
import numpy as np
import ast
ast.literal_eval("{'x':1, 'y':2}")


class W2CreateView(generics.CreateAPIView):
    queryset = W2.objects.all()
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

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


#시리얼라이저 쓰지 않고 만들기
class W2TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print("request.data: {}".format(request.data))
        name = request.data['name']
        # file_category = kwargs.get("w2_category")
        # user = request.user
        # user.taxpayerprofile_set.file_category.w2.img 으로 접근해서 file 가져오기

        file = storage.open("w2/2014.png")
        img = Image.open(file).convert("L")
        np_img = np.array(img)
        w2_autocomplete.delay(np_img, name)
        return Response({'status':'ok'}, status=status.HTTP_201_CREATED)






# @api_view(['POST'])
# def w2_auto_start(request):
#     user = request.user
#     try:
#         who = request.data['property']
#     except:
#         return Response({"message": "Error"},
#                         status=status.HTTP_200_OK)
#     if request.method == "POST":
#         # url = 나중에 유저 생성과 w2와 관련된 모델들이 다 작성되었을 때 제대로 생성 지금은 임시값
#         # url = user.taxpayerprofile_set.who.w2
#         file = storage.open("w2/2014.png")
#         img = Image.open(file).convert("L")
#         add_auto_queue(autocomplete, url=None, img=img)
#         return Response({"message": "Okay"})
#

# def add_auto_queue(func, *args, **kwargs):
#     job = django_rq.enqueue(func, *args, **kwargs)
#     task = Task.objects.create(
#         job_id=job.id,
#         name=kwargs.get('name', "not_defined")
#     )
#     task.result = "start"
#
#     if job.is_failed:
#         task.result = "failed"
#     else:
#         task.result = "Success"
#     task.save()
#     return task.result
# #
#
#
#             #
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