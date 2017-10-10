import numpy as np
from PIL import Image
from django.core.files.storage import default_storage as storage
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from autoinput.models import Task
from autoinput.serializers import TaskSerializer
from autoinput.task_func import w2_autocomplete

__all__ = ('W2TaskCreateView', )


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

