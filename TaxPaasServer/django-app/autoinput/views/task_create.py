import numpy as np
from PIL import Image
from django.core.files.storage import default_storage as storage
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from autoinput.models import Task, W2, Ten99INT, Ten99DIV
from autoinput.serializers import TaskSerializer
from autoinput.task_func import w2_autocomplete, int_autocomplete, \
    div_autocomplete
from member.models import TaxPayerProfile

__all__ = ('W2TaskCreateView2', "W2TaskCreateView", "IntTaskCreateView",
           "DivTaskCreateView")


# W2 Task Queue Create View
class W2TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        request.data._mutable = True

        request.data['category'] = kwargs["category"]
        request.data['doc_order'] = kwargs['doc_order']
        request.data['order'] = kwargs['order']
        source_doc = self.get_source_doc(request, *args, **kwargs)
        request.data['source_doc'] = source_doc.pk
        print(source_doc)
        print(source_doc.w2_set.all())
        if source_doc.w2_set.filter(order=request.data['order']).exists():
            w2 = source_doc.w2_set.filter(order=request.data['order'])[0]
        else:
            return Response({"errors": "요청하신 W2가 존재하지 않습니다"},
                            status=status.HTTP_404_NOT_FOUND)
        file = storage.open(w2.img.name)
        img = Image.open(file).convert("L")
        # img = resize_img(img, size)
        np_img = np.array(img)
        w2_autocomplete.delay(np_img, w2.pk)
        return Response({'status':'ok'}, status=status.HTTP_201_CREATED)

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

    def resize_img(self, size):
        pass


# W2 Task Queue Create View
class W2TaskCreateView2(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        pk = request.data['pk']
        w2 = get_object_or_404(W2, pk=pk)

        file = storage.open(w2.img.name)
        img = Image.open(file).convert("L")
        # img = resize_img(img, size)
        np_img = np.array(img)
        w2_autocomplete.delay(np_img, w2.pk)
        return Response({'status':'ok'}, status=status.HTTP_201_CREATED)

    def resize_img(self, size):
        pass


# Int Task Queue Create View

class IntTaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        pk = request.data['pk']
        int_obj = get_object_or_404(Ten99INT, pk=pk)

        file = storage.open(int_obj.img.name)
        img = Image.open(file)
        # img = resize_img(img, size)
        np_img = np.array(img)
        int_autocomplete.delay(np_img, int_obj.pk)
        return Response({'status':'ok'}, status=status.HTTP_201_CREATED)

    def resize_img(self, size):
        pass


# Div Task Queue Create View
class DivTaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        pk = request.data['pk']
        div = get_object_or_404(Ten99DIV, pk=pk)

        file = storage.open(div.img.name)
        img = Image.open(file)
        # img = resize_img(img, size)
        np_img = np.array(img)
        div_autocomplete.delay(np_img, div.pk)
        return Response({'status':'ok'}, status=status.HTTP_201_CREATED)

    def resize_img(self, size):
        pass

